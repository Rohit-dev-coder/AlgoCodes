#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

def sockMerchant(n, ar):
    dict = {}
    for no in ar:
        if no not in dict.keys():
            add = {no: ar.count(no)}
            dict.update(add)
    print(dict)
    pair = 0
    for v in dict.values():
        pair = pair + int(v/2)

    return int(pair)


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)