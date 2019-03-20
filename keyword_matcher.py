from collections import defaultdict
from difflib import get_close_matches
from tuples_data import *
import re



## Necessary in order to merge the multiple definitions that some words may have 
# Create a defaultdict object with a list as default factory
dictionary = defaultdict(list)

# Append the list-of-tuples values to the dictionary
for line in tuples_data:
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



def keyword_matcher():
    print("\nWelcome to Rado's dictionary service!\nSimply enter a word which you want to know the meaning of.\n")
    word = ""
    while word != "quit":
        word = raw_input("\nEnter word: ")
        if word == "quit":
            break
        status,lookup_res = lookup_word(word)
        alternatives = ""

        if status == 0:     # Suggest words with similar spelling
            if not lookup_res:      # Check if similar words were found
                print("No similar words were found!")
            else:
                for alternative in lookup_res:
                    alternatives += str(alternative) + ", "
                alternatives = alternatives[0:len(alternatives)-2]      # remove the comma and space afer the last word
                print("Word not found. Perhaps you meant one of these: " + str(alternatives) + "?")
        
        elif status == 1:       # Show definition(s) of the word
            for iteration,definition in enumerate(lookup_res):
                print("\n" + "Definition " + str(iteration+1) + ": " + definition)


def main():
    keyword_matcher()


if __name__=="__main__":
    main()