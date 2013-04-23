wordlist = []

def find_eights():
    for line in open('words.txt', 'r'):
        word = line.strip('\r\n')
        print len(word)
        if len(word) == 8:
            wordlist.append(word)
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

def find_anagrams(mydict):
    lett = (k for k in mydict)
    for x in lett:
        print mydict[lett.next()]

def sort_anagrams(mydict):
    anagrams_lists = []
    for k in mydict:
        anagrams_lists.append(mydict[k])
    anagrams_lists.sort(key=len, reverse=True)


    print "Most possible bingo"
    for i in range(2):
        print anagrams_lists[i]

words_dict = build_dict(wordlist)
sort_anagrams(words_dict)
