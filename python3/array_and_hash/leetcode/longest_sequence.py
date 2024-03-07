# 128
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


from typing import List

class Solution:
    def longestSequence(self, nums: List[int]) -> int:
        #  start of sequence has no left
        #   1 2 3 4    100    200

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of seq
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest



tests = [
    (
        # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        ([100,4,200,1,3,2],), # Input
        (4),            # Output
    ),
    (
        ([0,3,7,2,5,8,4,6,0,1],),
        (9),
    ),
]
