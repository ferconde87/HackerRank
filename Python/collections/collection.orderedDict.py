# from collections import OrderedDict
# n = int(input())
# d = OrderedDict()
# for _ in range(n):
#     line = input().split()
#     last_pos = len(line)-1
#     item_name = " ".join(line[:last_pos])
#     net_price = int(line[last_pos])
#     if item_name in d:
#         d[item_name] += net_price
#     else:
#         d[item_name] = net_price
# for item_name, net_price in d.items():
#     print(item_name, net_price)

from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    item_name, _, net_price = input().rpartition(" ")
    if item_name in d:
        d[item_name] += int(net_price)
    else:
        d[item_name] = int(net_price)
for item_name, net_price in d.items():
    print(item_name, net_price)
