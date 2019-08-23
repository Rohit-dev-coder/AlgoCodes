#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dict = {}
    for no in arr:
        if no not in dict.keys():
            add = {no: arr.count(no)}
            dict.update(add)
    mvalue = 0
    mkey = 0
    print(dict)
    for key,value in dict.items():
        if value > mvalue :
            mkey = key
            mvalue = value
        if value == mvalue:
            if mkey > key :
                mkey = key
                mvalue = value
    return mkey
if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
