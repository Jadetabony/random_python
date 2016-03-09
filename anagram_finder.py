"""Function anagram take a list of words, breaks them down into a 
list of a list of the individual characters. Then, each list within the new list is sorted.
Then list comprehension is used to create a list of indeces in for which there are 
duplicates in the sorted list.  Then I create one last list in which I take the 
values of original words list that correspond to the indeces in my indx list."""

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
