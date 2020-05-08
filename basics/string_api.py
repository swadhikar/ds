import random
import string

import cherrypy

get_random = lambda x: ''.join(random.sample(string.hexdigits, int(x))).lower()


@cherrypy.expose
class StringGeneratorApi:

    def PUT(self, new_str):
        cherrypy.session['mystring'] = new_str

    def POST(self, length=8):
        random_str = get_random(length)
        cherrypy.session['mystring'] = random_str
        return random_str

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']


if __name__ == '__main__':
    # cherrypy.quickstart(StringGeneratorApi())

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [
                ('Content-Type', 'text/plain')
            ]
        }
    }
    cherrypy.quickstart(StringGeneratorApi(), '/', conf)
