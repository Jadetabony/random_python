
input_list = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star']


def anagram1(words):
    letters =[]
    for item in words:
        char = []
        for c in item:
            char.append(c)
        letters.append(char)
    print letters

    sortd = []
    for lst in letters:
        lst.sort()
        sortd.append(lst)
    print sortd

    indx=[i for i, x in enumerate(sortd) if sortd.count(x) > 1]
    print indx

    final = []
    for i in indx:
        final.append(words[i])

    print "Final list:", final

anagram1(input_list)
