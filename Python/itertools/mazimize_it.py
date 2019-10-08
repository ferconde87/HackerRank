from itertools import product
k, m = map(int, input().split())
xxs = []
for _ in range(k):
    line = input().split()
    xs = list(map(int, line[1:len(line)]))
    xxs.append(xs)
result = 0
for item in list(product(*xxs)):
    current = (sum([x*x for x in list(item)])) % m
    if current > result:
        result = current
print(result)
