# 2300
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# Constraints:
# n == spells.length
# m == potions.length
# 1 <= n, m <= 105
# 1 <= spells[i], potions[i] <= 105
# 1 <= success <= 1010


from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions
        potions.sort() 
        pairs = []
        
        for s in spells:
            l, r = 0, len(potions)-1

            while l <= r: 
                m = (l+r) // 2
                product = s * potions[m]
                
                if product >= success: 
                    r = m - 1
                else: 
                    l = m + 1 

            pairs.append(len(potions)-l)

        return pairs

# Test cases
tests = [
    (
        ([5,1,3],[1,2,3,4,5],7,), # Input
        ([4,0,3]),  # Output
    ),
    (
        ([3,1,2],[8,5,8],16,), # Input
        ([2,0,2]),  # Output
    ),
]

            


                


