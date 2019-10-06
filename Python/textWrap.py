import textwrap

def wrap2(string, max_width):
    i = 0
    j = max_width
    result = ""
    while i < len(string):
        result += string[i:j]
        result += "\n"
        i += max_width
        j += max_width
    return result

def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
