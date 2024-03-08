#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0

    for idx, person in enumerate(q):
        if person - (idx + 1) > 2:
            return "Too chaotic"
        
        for j in range(max(0, person - 2), idx):
            if q[j] > person:
                bribes += 1

    return bribes


def test_minimumBribes():
    # Define test cases
    test_cases = [
        ([2, 1, 5, 3, 4], 3),  # Test case 1
        ([2, 5, 1, 3, 4], "Too chaotic"),  # Test case 2
        # Add more test cases as needed
    ]

    # Iterate over test cases
    for i, (q, expected) in enumerate(test_cases, 1):
        result = minimumBribes(q)
        assert result == expected, f"Test case {i} failed: Expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == '__main__':
    test_minimumBribes()
