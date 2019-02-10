from collections import defaultdict
from data import *

# with open('data.txt',"r") as f:
#     data = [line.strip() for line in f]


d = defaultdict(list)
print(data[1])

for line in data:
    for key,value in line:
        d[key].append(value)

# for item in d:
#     print(d)
#     break

# print(d)
# d = dict(d)
# print(d)



    # print("key: {}, value: {}".format( key, value))
    # while index < len(data) and data[index + 1] != key:
    #     inner_key = data[index + 1]
    #     data[key].append(data[inner_key])
    #     break


