#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    s = ''.join(sorted(s))
    counter = Counter()
    for c in s:
        counter[c] += 1
    for t in counter.most_common(3):
        print(*t)
