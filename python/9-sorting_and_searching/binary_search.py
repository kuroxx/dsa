# "leftmost binary search" (a.k.a left bisection)
# if target element exists, return the leftmost index
# else, return location of index

from typing import List

def binary_search(nums: List[int], target: int) -> int: 
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else: 
            right = mid 
    return left

nums = [1, 2, 3, 3, 3, 6, 9]
print("nums = " + str(nums))

print("=== target exists ===")
exists = [1,2,3,6,9]
for i in exists:
    print(f'index of {str(i)} = {str(binary_search(nums, i))}')
    # print("index of " + str(i) + " = " + str(binary_search(nums, i)))

print("=== target does not exist: index of where it should be ===")
not_exists = [0, -100, 4, 10, 100]
for i in not_exists:
    print("index of " + str(i) + " = " + str(binary_search(nums, i)))

print("=== verify target exists ===")
verify = [1,3,0,7,10]
for i in verify:
    index = binary_search(nums, i)
    contains = index < len(nums) and i == nums[index]
    print("nums contains " + str(i) + ": " + str(contains))
