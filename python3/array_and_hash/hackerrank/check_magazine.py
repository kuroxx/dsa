#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    # add whole words magazine to dict
    # check each letter in not against dict

    # m = "Ataack at dawn"
    # n = "attack at dawn"

    words = {}

    for m in magazine: 
        words[m] = 1 + words.get(m,0)

    for n in note:
        if n not in words:
            return "No"
        
        if words[n] == 1:
            del words[n]
        else:
            words[n] -= 1
    
    return "Yes"


def test_checkMagazine():
    test_cases = [
        (["give", "me", "one", "grand", "today", "night"], ["give", "one", "grand", "today"], "Yes"),  # Test case 1
        (["two", "times", "three", "is", "not", "four"], ["two", "times", "two", "is", "four"], "No"),  # Test case 2
        # Add more test cases as needed
    ]

    for i, (magazine, note, expected) in enumerate(test_cases, 1):
        result = checkMagazine(magazine, note)
        assert result == expected, f"Test case {i} failed: Expected {expected}, got {result}"

    print("All test cases passed!")

if __name__ == '__main__':
    test_checkMagazine()
