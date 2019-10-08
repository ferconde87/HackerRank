from collections import Counter

if __name__ == '__main__':
    nshoes = int(input())
    sizes = list(map(int, input().split()))
    ncustomers = int(input())
    shoes_size = Counter(sizes)
    result = 0
    for c in range(ncustomers):
        size, money = map(int, input().split())
        if shoes_size[size] > 0:
            shoes_size[size] -= 1
            result += money
    print(result)
