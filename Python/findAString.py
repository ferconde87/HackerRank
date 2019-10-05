def count_substring(string, sub_string):
    count = 0
    pos = 0
    n = len(string)
    m = len(sub_string)
    for i in range(n):
        pos = string.find(sub_string, pos, n)
        if pos == -1:
            break
        count += 1
        pos += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
