from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    line = input().split()
    if line[0] == "append":
        d.append(line[1])
    elif line[0] == "appendleft":
        d.appendleft(line[1])
    elif line[0] == "pop":
        d.pop()
    else:
        d.popleft()
print(*d)

