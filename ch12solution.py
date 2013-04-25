# solutions from http://epequeno.wordpress.com/2011/12/27/exercise-12-04/

words_file = open('words.txt', 'r')

def clean(myfile):
    '''Removes newlines from file read.'''
    return [line.strip('\r\n') for line in myfile]

words_list = clean(words_file)

def make_anagram_dict(mylist):
    fingerprints = dict()
    for word in mylist:
        fp = ''.join(sorted(word))
        if fp not in fingerprints:
            fingerprints[fp] = []

    for word in mylist:
        fp = ''.join(sorted(word))
        if fp in fingerprints:
            fingerprints[fp].append(word)

    return_dict = dict()
    for fp in fingerprints:
        if len(fingerprints[fp]) <= 1:
            pass
        else:
            return_dict[fp] = fingerprints[fp]

    return return_dict

words_dict = make_anagram_dict(words_list)

def print_anagrams(mydict):
    fp = (fp for fp in mydict)

    print "Sample from anagram dict:"
    i = 0
    while i < 5:
        next = fp.next()
        print "%s) %s:" % ((i + 1), next), mydict[next]
        i += 1

    print "..."
    print "\n"


print_anagrams(words_dict)

def sort_anagrams(mydict):
    anagrams_lists = []
    for fp in mydict:
        anagrams_lists.append(mydict[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    for i in range(0, 5):
        print "%s) " % (i + 1), anagrams_lists[i]
    print "..."
    print "\n"


sort_anagrams(words_dict)

def find_bingos(mydict):
    candidates = [mydict[key] for key in mydict if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print "Top Bingos:"
    for i in range(0, 5):
        print "%s) " % (i + 1), candidates[i]

    print "..."
    print "\n"

find_bingos(words_dict)

def is_metathesis(reference, test):
        if len(reference) != len(test):
            return False
        i = 0
        count = 0
        while i < (len(reference) - 1):
            if reference[i] != test[i]:
                count += 1
            i += 1
        if count == 2:
            return True
        return False


def find_metathesis(mydict):
    answer = []
    for fp in mydict:
        reference = mydict[fp][0]
        for i in range(1, (len(mydict[fp]) - 1)):
            test = mydict[fp][i]
            if is_metathesis(reference, test):
                answer.append([reference, test])

    print "Sample of metathesis pairs:"
    for i in range(0, 5):
        print "%s) " % (i + 1), answer[i]
    print "..."

find_metathesis(words_dict)
