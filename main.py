from collections import defaultdict
from data import *


# Create a defaultdict object with a list as default factory
d = defaultdict(list)

# Append the list-of-tuples values to the dictionary
for line in data:
    d[line[0]].append(line[1])