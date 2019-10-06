def print_formatted(number):
    width = len(bin(number).lstrip("0b"))
    for x in range(1,number+1):
        print(str(x).rjust(width),oct(x).lstrip("0o").rjust(width),hex(x).lstrip("0x").upper().rjust(width),bin(x).lstrip("0b").rjust(width))

def print_formatted2(N):
    width = len(bin(N)) - 2
    for i in range(1,N+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
