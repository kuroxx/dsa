# 11
# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List

class Solution: 
    def mostWater(self, height: List[int]) -> int:
        #  0 1 2 3 4 5 6 7 8 
        # [1,8,6,2,5,4,8,3,7]

        left, right = 0, len(height)-1
        maxArea = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return maxArea 


tests = [
    (
        # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        ([1,8,6,2,5,4,8,3,7],), # Input
        (49),            # Output
    ),
    (
        ([1,1],),
        (1),
    ),
]
