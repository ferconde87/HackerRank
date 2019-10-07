if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []
    for x in a:
        for y in b:
            result.append((x,y))
    print(*result)
