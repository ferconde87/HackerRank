t = int(input())
for _ in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    k = len(b.difference(a))
    print(k == (m-n))
#   print(a.issubset(b)) ;)

