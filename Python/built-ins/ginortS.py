string = input()
lowers = []
uppers  = []
odds = []
evens = []
for c in string:
    if c.islower():
        lowers.append(c)
    elif c.isupper():
        uppers.append(c)
    else:
        if int(c) % 2 == 1:
            odds.append(c)
        else:
            evens.append(c)
lowers = sorted(lowers)
uppers = sorted(uppers)
odds = sorted(odds)
evens = sorted(evens)
result = lowers + uppers + odds + evens
print("".join(result))
