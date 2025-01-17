# 242
# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
# O(nlogn+mlogm)
class Solution: 
    def validAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

tests = [
    (
        ("anagram","nagaram",),
        True,
    ),
    (
        ("rat","car",),
        False,
    ),
]
