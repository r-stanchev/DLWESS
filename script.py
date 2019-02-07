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

# # Read in the original dictionary
# with open("tmp.txt","r") as f:
#     raw = f.readlines()

# # The new file to save to
# with open("new.txt","w") as f2:
#     for line in raw:
#         if not line.strip():
#             f2.write(line)
#         else:
#             line = line.lstrip()
#             f2.write(line)




'''
This script deletes all occurrences of () with anything in between
'''

# import re

# # Read in the original dictionary
# with open("tmp.txt","r") as f:
#     raw = f.readlines()

# # The new file to save to
# with open("new.txt","w") as f2:
#     for line in raw:
#         print("BEFORE: " + str(line))
#         res = re.sub("\(.*?\)","",line)           
#         print("AFTER " + str(res))
#         f2.write(res)






'''
This script 
'''

import re

# Read in the original dictionary
with open("tmp.txt","r") as f:
    raw = f.readlines()
    length = len(raw)

# The new file to save to
with open("new.txt","w") as f2:
    for index, line in enumerate(raw):
        if not line.strip():
            if index < length - 1:
                next_ = raw[index + 1]            
            if index > 0:
                prev = raw[index - 1]
            f2.write(line)
        elif line.strip() and index < length - 1 and (not raw[index + 1].strip()):
            res = re.sub(r"\n"," ",line)           
            f2.write(res)
            