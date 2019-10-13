#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    dic = {}
    result = []
    for s in strings:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    for q in queries:
        if q in dic:
            result.append(dic[q])
        else:
            result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

