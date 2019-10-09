from collections import deque
import sys
T = int(input())
for _ in range(T):
    n = int(input())
    d = deque(list(map(int, input().split())))
    last = sys.maxsize
    while d:
        if last >= d[0] and last >= d[len(d)-1]:
            if d[0] > d[len(d)-1]:
                last = d.popleft()
            else:
                last = d.pop()
        else:
            break
    if d:
        print("No")
    else:
        print("Yes")
    


