from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(lambda:[-1])
for i in range(1,n+1):
    x = input()
    if x in a:
        a[x].append(i)
    else:
        a[x] = [i]
for _ in range(m):
    y = input()
    print(*a[y])
