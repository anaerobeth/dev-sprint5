# This is where the answers to Chapter 12 questions for the BSS Dev RampUp go
# Name: Elizabeth Tenorio

# Ex. 12.4
# 1. Write a program that reads a word list from a file (see Section 9.1)
# and prints all the sets of words that are anagrams

wordlist = [line.strip('\r\n') for line in open('words.txt', 'r')]

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
    # print uniques => returns the full dictionary
    return uniques

#words_dict = build_dict(wordlist)

def find_anagrams(mydict):
    lett = (k for k in mydict)
    # print lett => returns the object
    # print lett.next => returns method wraper
    # print lett.next() #=> returns the key

    for x in lett:
        print mydict[lett.next()]
    #lett_next = lett.next()


#find_anagrams(words_dict)
# sample results
# ['intervening', 'reinventing']
# ['gaol', 'goal']
# ['crumpets', 'spectrum'


# 2. Modify the previous program so that it prints the largest set of anagrams first,
# followed by the second largest set, and so on.

def sort_anagrams(mydict):
    anagrams_lists = []
    for k in mydict:
        anagrams_lists.append(mydict[k])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    for x in anagrams_lists:
        print x

#sort_anagrams(words_dict)
# sample results
# Most anagrams:
# ['alerts', 'alters', 'artels', 'estral', 'laster', 'ratels', 'salter', 'slater', 'staler', 'stelar', 'talers']
# ['apers', 'asper', 'pares', 'parse', 'pears', 'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']



# 3. In Scrabble a bingo is when you play all seven tiles in your rack,
# along with a letter on the board, to form an eight-letter word.
# What set of 8 letters forms the most possible bingos? Hint: there are seven.

def find_bingo(mydict):
    anagrams_lists = []
    for k in mydict:
        if len(k) == 8:
        #print k
        #print len(k)
            anagrams_lists.append(mydict[k])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    #for x in anagrams_lists:
    #    print x
    for i in range(8):
        print anagrams_lists[i]

words_dict = build_dict(wordlist)
find_bingo(words_dict)

# Sample result
# Most anagrams:
# ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']
# ['painters', 'pantries', 'pertains', 'pinaster', 'pristane', 'repaints']
# ['estrange', 'grantees', 'greatens', 'negaters', 'reagents', 'sergeant']
# ['aligners', 'engrails', 'nargiles', 'realigns', 'signaler', 'slangier']
# ['alerting', 'altering', 'integral', 'relating', 'tanglier', 'triangle']
# ['partlets', 'platters', 'prattles', 'splatter', 'sprattle']
# ['lameness', 'maleness', 'maneless', 'nameless', 'salesmen']
# ['pastries', 'piasters', 'piastres', 'raspiest', 'traipses']




