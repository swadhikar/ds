from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import datetime
import os

app = Flask(__name__)
basedir = os.path.join(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'marsh.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'date_created', '_links')

    _links = ma.Hyperlinks(
        {
            'self': ma.URLFor("user_detail", id="<id>"),
            "collection": ma.URLFor('users')
        }
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/api/users', methods=['GET'])
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


@app.route('/api/users/<id>', methods=['GET'])
def user_detail(id):
    user = User.query.get(id)
    print(f'returning:\n{user_schema.dump(user)}')
    return user_schema.dump(user)


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref="books")

    def __init__(self, title, author):
        self.title = title
        self.author = author


class AuthorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Author

    id = ma.auto_field()
    name = ma.auto_field()
    books = ma.List(ma.HyperlinkRelated('book_detail'))


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True

    author = ma.HyperlinkRelated("author_detail")


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/api/authors', methods=['GET'])
def authors():
    all_users = Author.query.all()
    result = authors_schema.dump(all_users)
    return jsonify(result)


@app.route('/api/authors/<id>', methods=['GET'])
def author_detail(id):
    user = Author.query.get(id)
    return author_schema.dump(user)


@app.route('/api/books', methods=['GET'])
def books():
    user = Book.query.all()
    res_ = books_schema.dump(user)
    return jsonify(res_)


@app.route('/api/book/<id>', methods=['GET'])
def book_detail(id):
    user = Book.query.get(id)
    return book_schema.dump(user)


@app.route('/api/book', methods=['POST'])
def add_book():
    dictionary = request.json

    # Get request messages
    book_name = dictionary['book']
    author_name = dictionary['author']

    # Create author
    author = Author(author_name)
    book = Book(book_name, author)

    # Check if author exists
    existing_author = Author.query.filter_by(name='author_name')
    if not existing_author:
        db.session.add(author)

    # Commit database
    db.session.add(book)
    db.session.commit()

    return book_schema.dump(book)


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

if __name__ == '__main__':
    app.run(debug=True)
