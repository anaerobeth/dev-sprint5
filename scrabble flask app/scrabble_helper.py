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


def find_bingo(mydict, target_length):
    anagrams_lists = []
    for k in mydict:
        if len(k) == target_length:
            anagrams_lists.append(mydict[k])
    return anagrams_lists.sort(key=len, reverse=True)


def hints(tiles, min_letters, target_length):
    words_dict = build_dict(wordlist)


if __name__ == '__main__':
