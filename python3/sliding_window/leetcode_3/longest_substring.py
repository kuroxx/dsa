# 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest 
# substring without repeating characters.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def longestSubstring(self, s: str) -> int: 
        left = 0
        longest = 0
        chars = set()

        for right in range(len(s)): 
            while s[right] in chars: 
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
            
    
tests = [
    (
        # Explanation: The answer is "abc", with the length of 3.
        ("abcabcbb",), # Input
        (3),            # Output
    ),
    (
        # Explanation: The answer is "b", with the length of 1.
        ("bbbbb",),
        (1),
    ),
    (
        # Explanation: The answer is "wke", with the length of 3.
        # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        ( "pwwkew",),
        (3),
    ),
]
 