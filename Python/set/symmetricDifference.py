def average(array):
    s = set(array)
    return sum(s)/len(s)

if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    c = a.difference(b).union(b.difference(a))
    c = list(c)
    c.sort()
    for x in c:
        print(x)

