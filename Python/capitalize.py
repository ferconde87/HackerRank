#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve2(s):
    ss = s.split()
    result = []
    for s in ss:
        result.append(s.capitalize())
    return " ".join(result)

def solve(s):
    result = []
    i = 0
    while i < len(s):
        while i < len(s) and s[i].isspace():
            result.append(" ")
            i += 1
        result.append(s[i].capitalize())
        i += 1
        while i < len(s) and not s[i].isspace():
            result.append(s[i].lower())
            i += 1
    return "".join(result)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
