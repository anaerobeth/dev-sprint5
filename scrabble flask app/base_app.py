# Week3 web app
# Name: Elizabeth Tenorio

import flask
import settings

#Views
from login import Login
from main import Main
from remote import Remote
from music import Music
from reverse import Reverse
from gallery import Gallery

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


#Routes
app.add_url_rule('/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/<page>/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/gallery/',
                view_func=Gallery.as_view('gallery'),
                methods=['GET'])
app.add_url_rule('/login/',
                view_func=Login.as_view('login'),
                methods=['GET', 'POST'])
app.add_url_rule('/remote/',
                view_func=Remote.as_view('remote'),
                methods=['GET', 'POST'])
app.add_url_rule('/reverse/',
                view_func=Reverse.as_view('reverse'),
                methods=['GET', 'POST'])
app.add_url_rule('/music/',
                view_func=Music.as_view('music'),
                methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
     return flask.render_template('404.html'), 404

app.debug = True
app.run()
