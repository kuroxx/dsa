# 238
# https://leetcode.com/problems/product-of-array-except-self/description/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

class Solution:
    def productArray(self, nums: List[int]) -> List[int]:
        #               1     2    3    4 
        # prefix sum    1     2    6   24 
        # postfix sum   24   24   12    4
        #               24   12    8    6  
       
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


tests = [
    (
        ([1,2,3,4],),   # Input
        ([24,12,8,6]),  # Output
    ),
    (
        ([-1,1,0,-3,3],),
        ([0,0,9,0,0]),
    ),
]
