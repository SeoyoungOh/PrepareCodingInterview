import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    hike_step = []
    valley = 0
    down_count = 0
    up_count = 0

    for step in s:
        if step == "D":
            down_count += 1
            if up_count != 0:
                down_count -= 1
                up_count -= 1

        else:
            up_count += 1
            if down_count != 0:
                up_count -= 1
                down_count -= 1
                if down_count == 0 and up_count == 0:
                    valley += 1

    return valley


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # s = input()
    # result = countingValleys(n, s)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    n = 8
    s = "UDDDUDUU"