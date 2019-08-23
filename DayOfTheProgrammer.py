#!/bin/python3

import math
import os
import random
import re
import sys

def isleapyear(year):
    if year % 4 != 0:
        return False;
    if year > 1918 and year % 100 == 0 and year % 400 != 0:
        return False;
    return True


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if isleapyear(year):
        print("leap year","12","09",year,sep = '.')
        return f"12.09.{year}"
    else:
        print("13","09",year,sep = '.')
        return f"13.09.{year}"

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)
