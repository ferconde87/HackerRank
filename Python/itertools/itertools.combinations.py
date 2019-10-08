from itertools import combinations
word, k = input().split()
word = ''.join(sorted(word))
k = int(k)
for i in range(1,k+1):
    ps = list(combinations(word,i))
    for p in ps:
        print("".join(p))
