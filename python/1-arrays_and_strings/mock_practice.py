# Given an array, find the longest contiguous subarray 
# and allow for 3 changes to integer values and return its length. 
# ([0-9] where n is the integer value in the array)

# [3, -3, 3, 3, 3, 1, -3]
# [1,3,3,3,3,5,6,7,3,3,3,] 
# [1,2,2,1,2,2,1,2,2,1,2,2,3,3,3,3,3,3]

# mock attempt
# Class Solution:
# 	Def search(self, nums: List[int], target: int) -> int:
# 		Left, change, right = 0, 0, len(nums) - 1
		
#         For idx, val in enumerate(nums):
#         If val != target: 
#         change = idx # first change

#     Def search2(self, nums: List[int], target: int) -> int:
#         Start, end = 0, len(nums) # not needed
#         for i in range(len(nums)):
#             For j in range(i, len(nums)):
#                 If nums[i] == target:
#                     Start = i
			
# feedback
# - write down the constraints
# - breakdown problem / simplify with assumptions
# - start with brute force solution first
# - identify repeated work and then optimize it


# Brute force O(n^2)
# -  for each val in arr, iterate through rest of arr to find max length

from typing import List

def longestSubarray(nums: List[int], flips: int) -> int:
    max_length = 0
    for i in range(len(nums)):
        count = {}
        count[nums[i]] = 1 + count.get(nums[i], 0)
        for j in range(i + 1, len(nums)):
            count[nums[j]] = 1 + count.get(nums[i], 0)
            max_freq = max(count.values())
            if (j - i + 1) - max_freq > flips:
                break
            max_length = max(max_length, j - i + 1) 
    return max_length

# print(longestSubarray([1,2,2,1,2,2], 1))

# Linear O(n) 
# - sliding window technique

def longestSubarray2(nums: List[int], flips: int) -> int:
    count = {}
    max_length = 0
    left = 0
    max_freq = 0

    for right in range(len(nums)):
        count[nums[right]] = 1 + count.get(nums[right], 0)
        max_freq = max(max_freq, count[nums[right]])

        while (right - left + 1) - max_freq > flips:
            count[nums[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length

print(longestSubarray2([1,2,2,1,2,2], 1))

#  i                 j
#  0  1  2  3  4  5  6
# [1, 2, 2, 1, 2, 2, 1, 3, 3, 3, 3, 3]


#  i                  j
#  0   1  2  3  4  5  6
# [3, -3, 3, 3, 3, 1, 3]
#      x 
