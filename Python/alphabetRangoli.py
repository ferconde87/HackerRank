def make_lines(index_letter, amount):
    abcd = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    cur = index_letter
    for i in range(amount - 1):
        result += abcd[cur] + '-'
        cur -= 1
    result += abcd[cur]
    for i in range(amount-1):
        cur += 1
        result += '-' + abcd[cur]
    return result

def print_rangoli(size):
    letters = size*2 - 1
    separators = letters - 1
    width = letters + separators
    lines = ""
    index_letter = size - 1
    for amount in range(1,size):
        lines += make_lines(index_letter, amount).center(width, '-') + "\n"
    mid_line = make_lines(index_letter, size)
    rlines = lines[::-1]

    print(lines + mid_line + rlines)


    

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
