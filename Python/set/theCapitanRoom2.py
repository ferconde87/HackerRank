k = int(input())
l = list(map(int, input().split()))
sum_l = sum(l)
sum_s = sum(set(l))*k
elem = (sum_s - sum_l) // (k-1)
print(elem)
