'''
This script removes all lines from "(1" to "(7" inclusive
'''

# Read in the original dictionary
with open("ldoce.txt","r") as f:
    raw = f.readlines()

# The new file to save to
with open("new.txt","w") as f2:
    for line in raw:
        line = line.lstrip()
        if  (not line.startswith("(1")) and \
            (not line.startswith("(2")) and \
            (not line.startswith("(3")) and \
            (not line.startswith("(4")) and \
            (not line.startswith("(5")) and \
            (not line.startswith("(6")) and \
            (not line.startswith("(7")):
            f2.write(line)


