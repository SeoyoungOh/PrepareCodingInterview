import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(0, d):
        out_number = a.pop(0)
        a.append(out_number)

    return a


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # nd = input().split()
    #
    # n = int(nd[0])
    # 
    # d = int(nd[1])
    #
    # a = list(map(int, input().rstrip().split()))
    #
    # result = rotLeft(a, d)
    #
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()

    d = 4
    a = [1, 2, 3, 4, 5]
    result = rotLeft(a, d)

    print("result : {}".format(result))

