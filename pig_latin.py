"""reads in a file specified by the user and translates into pig latin."""
import inflect

p = inflect.engine()

filename= raw_input("Please type a file name and hit return: ")
with open(filename) as f:
    content = f.readlines()

import string
import re

new_content = []
for line in content:
    words = line.split()
    for word in words:
        try:
            float(word)
            word = p.number_to_words(word)
            words = word.split()
            new_content.append(words)
        except ValueError:
            new_content.append(word)
#remove punctuation
no_punt= []
for word in new_content:
    if word[0] in string.punctuation:
        no_punt.append(word[0])
        no_punt.append(word[1:])
    else:
        no_punt.append(word)

no_punct= []
for word in no_punt:
    length = len(word)
    if word[length-1] in string.punctuation:
        no_punct.append(word[:length-1])
        no_punct.append(word[length-1])
    else:
        no_punct.append(word)

vowels = ["a","A","E","e","i","I","o","O","U","u"]
translation = []

for word in no_punct:
    if len(word)>0 and word[0] in string.punctuation:
        translation.append(word)
    else:
        for i in range(0,len(word)):
            if word[i] in vowels:
                pig_word = word[i:] + '-'+ word[:i] +'ay'
                translation.append(pig_word)
                break

print translation

print " ".join(translation)

f = open('translated.txt', 'w')
f.write(" ".join(translation))
f.close()
