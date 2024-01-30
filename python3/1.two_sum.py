"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force O(n^2)
        # compute all possible sums and compare against target
        # for i in range(0, len(nums) - 2):
        #     for j in range(1, len(nums) - 1):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        # hashmap O(n)
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if value in hashmap:
                return hashmap[value], index
            hashmap[diff] = index
