# finding the smallest/largest element

# average case O(n) 
#   it recurs only on the subarray that
#   contains the kth largest element
#   until there's only 1 element remaining
#   n + n/2 + n/4 + ... + 1 = 2n

# worst case O(n^2)
#   if the array is already sorted

from typing import List

def findKthLargest (nums: List[int], k: int) -> int:
    k = len(nums) - k
    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]

    return quickSelect(0, len(nums) - 1)

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
print(findKthLargest([3,2,1,5,6,4], 2))

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
