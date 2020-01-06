#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_arr = []
    for i in range(0, 16):
        row, column = divmod(i, 4)
        hourglass_sum = arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row + 1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]
        sum_arr.append(hourglass_sum)

    return max(sum_arr)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # arr = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # result = hourglassSum(arr)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]
    result = hourglassSum(arr)

    print("result : {}".format(result))