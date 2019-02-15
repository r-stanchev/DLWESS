'''
L D O C E 
This script removes all lines from "(1" to "(7" inclusive
'''

    # # Read in the original dictionary
    # with open("ldoce.txt","r") as f:
    #     raw = f.readlines()

    # # The new file to save to
    # with open("new.txt","w") as f2:
    #     for line in raw:
    #         line = line.lstrip()
    #         if  (not line.startswith("(1")) and \
    #             (not line.startswith("(2")) and \
    #             (not line.startswith("(3")) and \
    #             (not line.startswith("(4")) and \
    #             (not line.startswith("(5")) and \
    #             (not line.startswith("(6")) and \
    #             (not line.startswith("(7")):
    #             f2.write(line)





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
This script removes all the empty lines and writes a space in their respective new-line charater
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
with open("data.py","w") as f2:
    f2.write("# -*- coding: utf-8 -*- ")
    f2.write("\ndata = [\n")
    for line in raw:
        res = re.sub(r"  ","\" , \"",line,1)  
        res = "(\"" + res
        res = res[:len(res)-2] + "\"),\n"
        f2.write(res)
    f2.write("\n]")



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
                This is easyly done thorugh the text editor's find/replace functions.
'''