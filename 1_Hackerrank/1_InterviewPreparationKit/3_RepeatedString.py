#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_in = []
    a_count = 0

    for idx, char in enumerate(s):
        if char == "a":
            a_in.append(idx)

    quotient, remain = divmod(n, len(s))
    a_count += quotient * len(a_in)

    if remain != 0:
        for a_idx in a_in:
            if a_idx < remain:
                a_count +=1

    return a_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # n = int(input())
    # result = repeatedString(s, n)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    s = 10
    n = "aba"
