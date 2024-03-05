# 20
# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def validParenthese(self, s: str) -> bool: 
        # if not in hash, then it is left bracket
        # so push to stack 

        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }    
        stack = []

        for char in s: 
            if char in hashmap: 
                top = stack.pop() if stack else ''

                if top != hashmap[char]:
                    return False
            else: 
                stack.append(char) 

        if len(stack) > 0: return False
            
        return True
        
        
tests = [
    (
        ("()",), # Input
        (True),            # Output
    ),
    (
        ("()[]{}",),
        (True),
    ),
    (
        ("(]",),
        (False),
    ),
    (
        ("{[]}",),
        (True)
    ),
    (
        ("[",),
        (False)
    ),
    (
        ("]",),
        (False)
    )
]
