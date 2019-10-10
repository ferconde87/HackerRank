from math import atan2, degrees
ab = int(input())
bc = int(input())
d = degrees(atan2(ab,bc))
print(str(round(d))+'°')
