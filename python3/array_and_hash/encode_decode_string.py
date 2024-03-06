# 659
# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode

# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


from typing import List

class Solution:
    def encode(self, string: List[str]) -> str:
        res = ""
        for s in string:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, string: str) -> List[str]:
        res = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            i = j + 1 + length
            res.append(string[ j + 1 : i])
        return res


# Test code
solution = Solution()

# Test encoding
input_strings = ["hello", "world", "python"]
encoded_string = solution.encode(input_strings)
print("Encoded string:", encoded_string)

# Test decoding
decoded_strings = solution.decode(encoded_string)
print("Decoded strings:", decoded_strings)

# Check if encoding and decoding are consistent
assert input_strings == decoded_strings, "Encoding and decoding are inconsistent"
print("Encoding and decoding are consistent")


# tests = [
#     (
#         # Explanation: one possible method is: "lint:;code:;love:;you"
#         (["neet","code","love","you"],),   # Input
#         (["neet","code","love","you"]),  # Output
#     ),
#     (
#         (["we","say",":","yes"],),
#         (["we","say",":","yes"]),
#     ),
# ]
