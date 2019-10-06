def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin "+str(kevin))
    elif stuart > kevin:
        print("Stuart "+str(stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
