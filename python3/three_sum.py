# 15
# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force O(n^3), add every possible combination

        # Sort first
        #      i  j            k
        # -1  -1  0  1  2  2  -4

        nums.sort()
        res = []

        for idx, val in enumerate(nums): 
            # don't use same value
            if idx > 0 and val == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r: 
                three_sum = val + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0: 
                    l += 1
                else: 
                    res.append([val, nums[l], nums[r]])
                    l += 1 
                    
                    # check if same value again i.e. [-2, -2, 0, 0, 2, 2]
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
                
        return res

tests = [
    (
        # Explanation: 
        # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        # The distinct triplets are [-1,0,1] and [-1,-1,2].
        # Notice that the order of the output and the order of the triplets does not matter.
        ([-1,0,1,2,-1,-4],), # Input
        ([[-1,-1,2],[-1,0,1]]),            # Output
    ),
    (
        # Explanation: The only possible triplet does not sum up to 0.
        ([0,1,1],),
        ([]),
    ),
    (
        # Explanation: The only possible triplet sums up to 0.
        ([0,0,0],),
        ([[0,0,0]]),
    ),
]
