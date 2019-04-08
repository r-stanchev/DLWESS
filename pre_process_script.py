'''
This script deletes the white spaces in the beginning of every line.
It leaves empty lines unchanged.
'''

# Read in the original dictionary
with open("azdictionary.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("new.txt","w") as f2:
    for line in raw:
        if not line.strip():
            f2.write(line)
        else:
            line = line.lstrip()
            f2.write(line)




'''
This script removes all the empty lines and writes a space instead of their respective new-line charater
'''

import re

# Read in the original dictionary
with open("new.txt","r") as f:
    raw = f.readlines()
    length = len(raw)

# The new file to save to
with open("new.txt","w") as f2:
    for line in raw:
        if not line.strip():
            f2.write(line)
        else:
            res = re.sub(r"\n"," ",line)           
            f2.write(res)




'''
This script deletes all occurrences of () with anything in between
'''

import re

# Read in the original dictionary
with open("new.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("new.txt","w") as f2:
    for line in raw:
        res = re.sub("\(.*?\)","",line)           
        f2.write(res)




'''
This script deletes all occurrences of "" with anything in between
as well as the single " 
'''

import re

# Read in the original dictionary
with open("new.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("new.txt","w") as f2:
    for line in raw:
        res = re.sub("\".*?\"","",line)
        res = re.sub("\"","",res)           
        f2.write(res)



'''
This script places double quotes around the dictionary keys and values 
and it transforms each word-definition entry to a tuple.
'''

import re

# Read in the original dictionary
with open("new.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("tuples_data.py","w") as f2:
    f2.write("# -*- coding: utf-8 -*- ")
    f2.write("\ntuples_data = [\n")
    for line in raw:
        res = re.sub(r"  ","\" , \"",line,1)  
        res = "(\"" + res
        res = res[:len(res)-2] + "\"),\n"
        f2.write(res)
    f2.write("\n]")




from collections import defaultdict
from tuples_data import *

## Necessary in order to merge the multiple definitions that some words may have 
# Create a defaultdict object with a list as default factory
dictionary = defaultdict(list)

# Append the list-of-tuples values to the dictionary
for line in tuples_data:
    dictionary[line[0]].append(line[1])


'''
Looks up a word in the dictionary and returns the definition(s) of the
word 
'''
def lookup_word(word):
    word = word.capitalize()
    return (dictionary[word])


'''
Replaces the definitions of words, which have the following definitions:
    See...
    Alt. of...
    of...
    Same as...
    pret. of...

with either the definitions of the words they reference or an empty line when needed
'''

for i in range(5):
    temp_refined_data = []
    for line in tuples_data:
        if not line[1]:     # Skip words which have no definitions
            continue
        res = line[1].split(' ')

        # Alt. of...
        if res[0] == "Alt." and res[1] == "of":
            target_word = re.sub('[!.,@#$]', '', res[2])
            target_definition = lookup_word(target_word)
            temp_refined_data.append((line[0],''.join(target_definition)))
        
        # Same as...
        elif res[0] == "Same" and res[1] == "as" and len(res) > 2:
            target_word = re.sub('[!.,@#$]', '', res[2])
            target_definition = lookup_word(target_word)
            temp_refined_data.append((line[0],''.join(target_definition)))
        
        # of...
        elif res[0] == "of":
            continue
        
        # pret. of...
        elif res[0] == "pret." and res[1] == "of":
            target_word = re.sub('[!.,@#$]', '', res[2])
            target_definition = lookup_word(target_word)
            temp_refined_data.append((line[0],''.join(target_definition)))
        
        # See...
        elif res[0] == "See":
            target_word = re.sub('[!.,@#$]', '', res[1])
            target_definition = lookup_word(target_word)
            temp_refined_data.append((line[0],''.join(target_definition)))
        else:
            temp_refined_data.append((line[0],line[1]))
    data = list(temp_refined_data)


with open("temp.txt","w") as f:
    for item in data:
        f.write("%s\n" % (item,))


import os
os.remove("new.txt")
# os.remove("data.py")


'''
This script places double quotes around the dictionary keys-values pair 
and it transforms each word-definition pair into a list.
'''

import re

# Read in the original dictionary
with open("temp.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("data.py","w") as f2:
    f2.write("# -*- coding: utf-8 -*- ")
    f2.write("\ndata = [\n")
    for line in raw:
        # Turns each round brace into a square bracket;
        # Replaces all single quotes with double ones 
        res = re.sub(r"\(\"","[\"",line,1)
        res = re.sub(r"\(\'","[\"",res,1)

        # Remove the comma between word and definition, essentially joining the two strings
        res = re.sub("\'\, \'"," ",res,1)
        res = re.sub("\'\, \""," ",res,1)
        res = re.sub("\"\, \'"," ",res,1)
        res = re.sub("\"\, \""," ",res,1)
        
        # Turns each round brace into a square bracket;
        # Replaces all single quotes with double ones 
        res = re.sub(r"\"\)","\"],",res,1)
        res = re.sub(r"\'\)","\"],",res,1)
        f2.write(res)
    f2.write("\n]")

os.remove("temp.txt")


'''
                After running these scripts on the the file "azdictionary.txt" I had to manually delete
                a couple of lines which were preventing for the rest of the entries to be in dictionary 
                format. 

                                                UPDATE 1: 
                I removed the problematic lines from the original "azdictionary.txt" file so
                there is no need to delete them after the pre-processing step each time. 
                The end-ruslt file is a .py file. In order to work with this dictionary, it is
                neccessary to first convert the tuples to a list(place angle brackets around them 
                and name the lsit) and import the file wherever it is going to be used.

                                                UPDATE 2:
                Need to remove all instances of   /.    and     /,    after the scipt finishes.
                This is easily done thorugh the text editor's find/replace functions.


                                                UPDATE 3:
                Line 87317 has double closing brackets. Need to delete one of them.
                
'''