# https://neetcode.io/problems/singlyLinkedList

# Design a Singly Linked List class.

import unittest
from typing import List

# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Dummy node
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            # Move current to node before target node
            i += 1
            current = current.next

        # Remove the node ahead of current
        if current and current.next:
            if current.next == self.tail: 
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res

# Example 1
#   Input: 
#   ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
#   Output:
#   [null, null, null, true, [0, 2]]

# Example 2
#    Input:
#    ["insertHead", 1, "insertHead", 2, "get", 5]
#    Output:
#    [null, null, -1]

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_example_1(self):
        self.ll.insertHead(1)
        self.ll.insertTail(2)
        self.ll.insertHead(0)
        self.assertTrue(self.ll.remove(1))
        self.assertEqual(self.ll.getValues(), [0, 2])

    def test_example_2(self):
        self.ll.insertHead(1)
        self.ll.insertHead(2)
        self.assertEqual(self.ll.get(5), -1)

if __name__ == '__main__':
    unittest.main()
