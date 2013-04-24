import flask, flask.views
import os

class Scrabble_helper(flask.views.MethodView):
    def get_words():
        wordlist = [line.strip('\r\n') for line in open('words.txt', 'r')]
        return wordlist

    def sort_string(word):
        letters = list(word)
        letters.sort()
        letters = ''.join(letters)
        return letters

    def build_dict(wordlist):
        letter_dict = dict()
        for word in wordlist:
            lett = sort_string(word)
            if lett not in letter_dict:
                letter_dict[lett] = []
            if lett in letter_dict:
                letter_dict[lett].append(word)

        uniques = dict()
        for lett in letter_dict:
            if len(letter_dict[lett]) <= 1:
                pass
            else:
                uniques[lett] = letter_dict[lett]
        return uniques


    def find_words(mydict):
        anagrams_lists = []
        for k in mydict:
            anagrams_lists.append(mydict[k])
        return anagrams_lists.sort(key=len, reverse=True)
