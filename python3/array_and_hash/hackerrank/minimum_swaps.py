#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0
    
    for i in range(len(arr)):
        while arr[i] != i + 1: 
            tmp = arr[i] - 1
            arr[i], arr[tmp] = arr[tmp], arr[i]
            swap_count += 1

    return swap_count


def test_minimumSwaps():
    test_cases = [
        ([4, 3, 1, 2], 3),  # Test case 1
        ([1, 3, 5, 2, 4, 6, 7], 3),  # Test case 2
        # Add more test cases as needed
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = minimumSwaps(arr)
        assert result == expected, f"Test case {i} failed: Expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == '__main__':
    test_minimumSwaps()
