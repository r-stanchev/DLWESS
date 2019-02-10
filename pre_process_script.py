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
'''

import re

# Read in the original dictionary
with open("new.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("data.txt","w") as f2:
    for line in raw:
        res = re.sub(r"  ","\" , \"",line,1)  
        res = "(\"" + res
        res = res[:len(res)-2] + "\"),\n"
        f2.write(res)
            


'''
                After running these scripts on the the file "azdictionary.txt" I had to manually delete
                a couple of lines which were preventing for the rest of the entries to be in dictionary 
                format. 
'''