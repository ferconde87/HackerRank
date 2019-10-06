def hasanyalphanumeric(s):
    for c in s:
        if c.isalnum():
            return True
    return False

def hasanyalphabetic(s):
    for c in s:
        if c.isalpha():
            return True
    return False

def hasanydigit(s):
    for c in s:
        if c.isdigit():
            return True
    return False

def hasanylower(s):
    for c in s:
        if c.islower():
            return True
    return False

def hasanyupper(s):
    for c in s:
        if c.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
    print(hasanyalphanumeric(s))
    print(hasanyalphabetic(s))
    print(hasanydigit(s))
    print(hasanylower(s))
    print(hasanyupper(s))
