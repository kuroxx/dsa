#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # hourglass = [a, b, c, d, e, f, g]
    # a, b, c
    #    d
    # e, f, g
    
    rows, cols = len(arr), len(arr[0])
    # a, b, c, d, e, f, g = 0,0,0,0,0,0
    max_sum = float('-inf')

    for i in range(rows - 2):
        for j in range(cols-2):

            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            
            hourglass_sum = sum([a,b,c,d,e,f,g])
            max_sum = max(max_sum, hourglass_sum)

    print(max_sum)
    return max_sum
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr = [ [-9, -9, -9,  1, 1, 1],
    #         [ 0, -9,  0,  4, 3, 2],
    #         [-9, -9, -9,  1, 2, 3],
    #         [ 0,  0,  8,  6, 6, 0],
    #         [ 0,  0,  0, -2, 0, 0],
    #         [ 0,  0,  1,  2, 4, 0] ]
    
    arr = [ [-1, -1,  0, -9, -2, -2],
            [-2, -1, -6, -8, -2, -5],
            [-1, -1, -1, -2, -3, -4],
            [-1, -9, -2, -4, -4, -5],
            [-7, -3, -3, -2, -9, -9],
            [-1, -3, -1, -2, -4, -5] ]
        
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
