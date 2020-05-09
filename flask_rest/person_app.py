from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import datetime
import os

app = Flask(__name__)
basedir = os.path.join(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('id', 'name', 'address', 'date_created')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)


@app.route('/person', methods=['GET'])
def get_people():
    people = Person.query.all()
    result = persons_schema.dump(people)
    return jsonify(result)


@app.route('/person/<id>', methods=['GET'])
def get_people_by_id(id):
    people = Person.query.get(id)
    return person_schema.jsonify(people)


@app.route('/person', methods=['POST'])
def post_person():
    name = request.json['name']
    address = request.json['address']

    person = Person(name=name, address=address)
    db.session.add(person)
    db.session.commit()
    return person_schema.jsonify(person)


@app.route('/person/<id>', methods=['DELETE'])
def remove_person(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': f'Deleted person - {person.id}: {person.name}'})


@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)

    name = request.json['name']
    address = request.json['address']

    person.name = name
    person.address = address
    db.session.commit()
    return person_schema.jsonify(person)


if __name__ == '__main__':
    app.run(debug=True)
