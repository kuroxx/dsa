# 49
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force is 2 for loops
        # check each str and pop if match

        #   0      1
        # ["eat","tea","tan"]

        #  aet    aet   ant
        # if sorted(1) == current_sorted

        # hashmap = {
        # aet: index 0
        # ant: index 1
        # }

        # sort nlogn

        # hashmap O(n)
        anagrams = []
        hashmap = {}
        index = 0
        
        for val in strs:
            word = ''.join(sorted(val))
            if word in hashmap:
                anagrams[hashmap[word]].append(val)
            else:
                hashmap[word] = index
                anagrams.append([val])
                index += 1
        return anagrams


tests = [
    (
        (["eat","tea","tan","ate","nat","bat"],),       # Input
        ([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),  # Output
    ),
    (
        ([""],),
        ([[""]]),
    ),
    (
        (["a"],),
        ([["a"]]),
    ),
]
