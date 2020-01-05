import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step_count = 0
    while len(c) > 1:
        if len(c) == 2:
            c.clear()
        else:
            if bool(c[2]):
                c.pop(c[0])
            else:
                c.pop(c[0])
                c.pop(c[1])
        step_count += 1

    return step_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # c = list(map(int, input().rstrip().split()))
    # result = jumpingOnClouds(c)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
    result = jumpingOnClouds(c)
    print("result : {}".format(result))