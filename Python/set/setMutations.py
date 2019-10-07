n = int(input())
a = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    command = input().split()
    b = set(map(int, input().split()))
    if command[0] == "intersection_update":
        a.intersection_update(b)
    elif command[0] == "update":
        a.update(b)
    elif command[0] == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    else:
        a.difference_update(b)
print(sum(a))
