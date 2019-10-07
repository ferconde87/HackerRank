n = int(input())
a = list(map(int, input().split()))
s = set()
result = set()
for x in a:
    if x not in s:
        s.add(x)
        result.add(x)
    else:
        result.discard(x)

print(result.pop())

