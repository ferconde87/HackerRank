# from itertools import permutations
# line = input().split()
# word = line[0]
# word = ''.join(sorted(word))
# k = int(line[1])
# ps = list(permutations(word,k))
# for p in ps:
#     for elem in p:
#         print(elem, end='')
#     print()

from itertools import permutations
word, k = input().split()
word = ''.join(sorted(word))
k = int(k)
ps = list(permutations(word,k))
for p in ps:
    print("".join(p))
