import flask, flask.views
import os

class Rack(flask.views.MethodView):
    def get(self):
        return flask.render_template("rack.html")

    def post(self):
        letters = str(flask.request.form['letters'])
        letters = list(letters)
        # letters.sort()
        # letters = ''.join(letters)

        # wordlist = [line.strip('\r\n') for line in open('words.txt', 'r')]

        # letter_dict = dict()
        # for word in wordlist:
        #     lett = list(letters)
        #     lett.sort()
        #     lett = ''.join(lett)

        #     if lett not in letter_dict:
        #         letter_dict[lett] = []
        #     if lett in letter_dict:
        #         letter_dict[lett].append(word)

        # uniques = dict()
        # for lett in letter_dict:
        #     if len(letter_dict[lett]) <= 1:
        #         pass
        #     else:
        #         uniques[lett] = letter_dict[lett]

        # suggested_words = []
        # for k in uniques:
        #     suggested_words.append(uniques[k])

        # suggested_words = []
        # for k in letter_dict:
        #     suggested_words.append(letter_dict[k])

        # suggested_words.sort(key=len, reverse=True)


        flask.flash(letters)
        return flask.redirect(flask.url_for('rack'))



