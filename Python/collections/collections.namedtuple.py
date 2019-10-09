# 1
# n = int(input())
# index = (input().split()).index("MARKS")
# avg = 0
# for _ in range(n):
#     l = list(input().split())
#     avg += int(l[index])
# print(avg/n)

# 2
# n = int(input())
# index = (input().split()).index("MARKS")
# print(sum(float(list(input().split())[index]) for _ in range(n))/n)

from collections import namedtuple
N = int(input())
student = namedtuple('student',input().split())
print(sum(float(student(*input().split()).MARKS) for _ in range(N))/N)
