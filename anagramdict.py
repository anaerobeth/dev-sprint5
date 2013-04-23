# wordlist = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
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

    return uniques

words_dict = build_dict(wordlist)

def find_anagrams(mydict):
    fp = (fp for fp in mydict)
    print "Anagrams found!"
    for i in range(1,3):
        fp_next = fp.next()
        print "%s) %s:" % (i, fp_next) , mydict[fp_next]


find_anagrams(words_dict)
