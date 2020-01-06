import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    is_chaotic = False
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            is_chaotic = True
            break
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    if is_chaotic:
        print("Too chaotic")
    else:
        print(moves)


if __name__ == '__main__':
    # t = int(input())
    # for t_itr in range(t):
    #     n = int(input())
    #     q = list(map(int, input().rstrip().split()))
    #     minimumBribes(q)

    q = [2, 1, 5, 3, 4]
    minimumBribes(q)