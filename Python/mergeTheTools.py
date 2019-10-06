from collections import OrderedDict 

def removeDuplicates(string):
    return "".join(OrderedDict.fromkeys(string))

def merge_the_tools(string, k):
    slices = len(string) // k
    l = 0
    for i in range(slices):
        segment = string[l:l+k]
        print(removeDuplicates(segment))
        l += k


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
