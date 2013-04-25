import flask, flask.views
import os

class Rack(flask.views.MethodView):
    global make_word_dict, signature, all_possibilities, d, p

    def get(self):
        return flask.render_template("rack.html")

    def make_word_dict(l):
        scrabble_dict = {}
        for letter in l:
            if letter in scrabble_dict:
                scrabble_dict[letter] = scrabble_dict[letter] + 1
            else:
                scrabble_dict[letter] = 1
        return scrabble_dict


    def signature(s):
        t = list(s)
        scrabble_dict = make_word_dict(t)
        return scrabble_dict

    def all_possibilities(filename, scrabble_letters, min_num_letters, total_word_length):

        d = []
        for line in open(filename):
            word = line.strip().lower()
            list_word = list(word)
            word_dict = make_word_dict(list_word)
            for i in scrabble_letters.keys():
                if i in word_dict:
                    if word_dict[i] > 1:
                        word_dict[i] = word_dict[i]-1
                    else:
                        word_dict.pop(i)
            nums_list = word_dict.values()
            ct = 0
            for x in nums_list:
                ct = ct + x
            if (len(list_word) - ct) > min_num_letters and len(list_word) < total_word_length:
                d.append(word)
        return d

    def post(self):
        scrabble_letters = str(flask.request.form['letters'])
        #scrabble_letters = 'catapult'
        scrabble_sig = signature(scrabble_letters)
        d = all_possibilities('words.txt', scrabble_sig, 5, 9)


        flask.flash(d)
        return flask.redirect(flask.url_for('rack'))


# if __name__ == "__rack__":
#     rack()
