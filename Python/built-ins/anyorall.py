# n = int(input())
# a = list(map(int, input().split()))
# print(all([x > 0 for x in a]) and any([str(x) == "".join(reversed(str(x))) for x in a]))

n = int(input())
a = list(map(int, input().split()))
print(all([x > 0 for x in a]) and any([str(x) == str(x)[::-1] for x in a]))
