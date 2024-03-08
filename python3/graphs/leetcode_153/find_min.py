# 153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

from typing import List

class Solution: 
    def findMin(self, nums: List[int]) -> int: 
        ans = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else: 
                r = m - 1
        
        return ans


tests = [
    (
        # Explanation: The original array was [1,2,3,4,5] rotated 3 times.
        ([3,4,5,1,2],), # Input
        (1),            # Output
    ),
    (
        # Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
        ([4,5,6,7,0,1,2],),
        (0),
    ),
    (
        # Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
        ([11,13,15,17],),
        (11),
    ),
]
