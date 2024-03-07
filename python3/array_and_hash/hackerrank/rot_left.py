#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    #       0 1 2 3 4 
    # a = [ 1 2 3 4 5 ]         d = 3

    # solution 1:
    # for i in range(d):
    #     tmp = a[0]
    #     del a[0]
    #     a.append(tmp)
    # return a

    # solution 2:
    d = d % len(a) # 13 % 3 = remainder 1
    n = a[d:] + a[:d]
    return n


def test_rotLeft():
    # Define test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),  # Test case 1
        ([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10, [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]),  # Test case 2
        # ...
    ]

    for i, (a, d, expected) in enumerate(test_cases, 1):
        result = rotLeft(a, d)
        assert result == expected, f"Test case {i} failed: Expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == '__main__':
    test_rotLeft()
