from itertools import combinations_with_replacement
word, k = input().split()

# word = ''.join(sorted(word))
# k = int(k)
# ps = list(combinations_with_replacement(word,k))
# for p in ps:
#     print("".join(p))

for p in list(combinations_with_replacement(''.join(sorted(word)),int(k))):
    print("".join(p))
