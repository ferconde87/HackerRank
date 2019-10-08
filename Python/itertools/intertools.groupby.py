from itertools import groupby
sgroupby = groupby(map(int, input()))
for key, it in sgroupby:
    print(tuple([len(list(it)), key]) ,end = " ")

from itertools import groupby
sgroupby = groupby(input())
for key, it in sgroupby:
    print("("+str(len(list(it)))+", "+key+")", end=" ") 

