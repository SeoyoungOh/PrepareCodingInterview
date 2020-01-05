import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_dic = {}
    current_pair = 0

    for color in ar:
        if color in pair_dic.keys():
            pair_dic[color] += 1
            if pair_dic[color] == 2:
                current_pair += 1
                pair_dic[color] -= 2

        else:
            pair_dic[color] = 1

    print(pair_dic)
    print(current_pair)

    return current_pair


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    # result = sockMerchant(n, ar)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print("result : {}".format(result))