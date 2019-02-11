from collections import defaultdict
from data import *
from difflib import get_close_matches


# Create a defaultdict object with a list as default factory
dictionary = defaultdict(list)

# Append the list-of-tuples values to the dictionary
for line in data:
    dictionary[line[0]].append(line[1])




'''
Looks up a word in the dictionary and returns either the definition(s) of the
word or a list with words which have a similar spelling (in addition to a numeric
value representing a status code, used later for determining what is returned)
'''
def lookup_word(word):
    word = word.capitalize()
    if word not in dictionary:
        similar_words = get_close_matches(word,dictionary.keys(),3)
        return (0,similar_words)
    else:
        return (1,dictionary[word])




print("\nWelcome to Rado's dictionary service!\nSimply enter a word which you want to know the meaning of.\n")
word = raw_input("Enter word: ")

status,lookup_res = lookup_word(word)
alternatives = ""
if status == 0:
    for alternative in lookup_res:
        alternatives += str(alternative) + ", "
    alternatives = alternatives[0:len(alternatives)-2]
    print("Word not found. Perhaps you meant one of these: " + str(alternatives) + "?")
elif status == 1:
    for definition in lookup_res:
        print(definition + "\n")





