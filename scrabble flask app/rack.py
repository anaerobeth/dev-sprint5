import flask, flask.views
import os

class Rack(flask.views.MethodView):
    def get(self):
        return flask.render_template("rack.html")

    def post(self):
        s = eval(flask.request.form['letters'])
        words_dict = build_dict(wordlist)
        result = find_bingo(words_dict)
        flask.flash(result)
        return flask.redirect(flask.url_for('rack'))
