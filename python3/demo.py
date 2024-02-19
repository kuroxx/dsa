# Use this library for quicker testing
#   https://github.com/tusharsadhwani/python_leetcode_runner
#   usage: pyleet <file-name>.py 

# Alternative: https://stackoverflow.com/questions/62614490/how-do-i-properly-input-my-own-test-cases-in-my-own-ide-for-problems-in-leetcode


class Solution:
    def demo(self, x: int, y: int) -> int:
        return x + y

tests = [
    (
        (2, 4,),      # input tuple
        6,            # output
    ),
    (
        (45, 67,),    # input tuple
        112,          # output
    ),
]
