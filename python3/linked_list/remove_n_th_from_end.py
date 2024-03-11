# 19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        # reverse ll not fast enough
        # so use two pointer technique

        dummy = ListNode(0, head)
        left = dummy
        right = head

        # find target node 
        while n > 0 and right: 
            right = right.next
            n -= 1

        while right: 
            left = left.next
            right = right.next

        # delete the node 
        left.next = left.next.next
        return dummy.next


# Test cases
tests = [
    (
        ([1,2,3,4,5],2,), # Input
        ([1,2,3,5]),  # Output
    ),
    (
        ([1],1,),
        ([]),
    ),
    (
        ([1,2],1,),
        ([1]),
    ),
]
