#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    socks = {}
    total = 0
    for sock in ar:
        if sock not in socks:
            socks[sock] = 1
        else:
            socks[sock] += 1
            if socks[sock] == 2:
                socks[sock] = 0
                total += 1
    return total


def sol2(n, ar):
    c = Counter()
    for i in ar:
        c[i] = c.get(i, 0) + 1
    c
    c[20] // 3
    return (sum([c[i]//2 for i in c]))


def sol3(n, ar):
    socks = Counter(input().split())
    print(sum(map(lambda x: x//2, socks.values())))


def sol4(n, ar):
    A = set(socks)
    for element in A:
        pairs += socks.count(element) // 2
    print(pairs)


if __name__ == '__main__':
    test_file = 'test_1.txt'
    fptr = open(test_file, 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
