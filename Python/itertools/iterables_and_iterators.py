from itertools import combinations
n = int(input())
arr = input().split()
k = int(input())
cs = list(combinations(arr, k))
count = 0
for c in cs:
    if 'a' in c:
        count += 1
print(count/len(cs))
