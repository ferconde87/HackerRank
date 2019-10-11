import re
t = int(input())
for _ in range(t):
    expression = input()
    isValid = True
    try:
        re.compile(expression)
    except re.error:
        isValid = False
    print(isValid)



