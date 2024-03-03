# 347
# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List

class Solution:
    def topKFrequentElements(self, nums: List[int], k: int) -> List[int]:
        # sort arr and iterate through

        res = []
        hashmap = {}

        for n in nums: 
            hashmap[n] = 1 + hashmap.get(n, 0)
            
        for i in range(k):
            max_freq = max(hashmap, key=hashmap.get)
            res.append(max_freq)
            del hashmap[max_freq]

        return res


tests = [
    (
        ([1,1,1,2,2,3],2,),       # Input
        ([1,2]),  # Output
    ),
    (
        ([1],1,),
        ([1]),
    ),
]
