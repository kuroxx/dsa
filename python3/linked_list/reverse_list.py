# 206
# https://leetcode.com/problems/reverse-linked-list/

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # iterative
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    # recursive
    def reverseListRecursively(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        reversed_list = self.reverseListRecursively(head.next)

        head.next.next = head
        head.next = None

        return reversed_list


# Test cases
tests = [
    (
        ([1,2,3,4,5],), # Input
        ([5,4,3,2,1]),  # Output
    ),
    (
        ([1,2],),
        ([2,1]),
    ),
    (
        ([],),
        (None),
    ),
]
