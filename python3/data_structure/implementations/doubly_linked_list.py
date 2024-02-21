# https://neetcode.io/problems/queue

# Design a Double-ended Queue class.
# Note: You should implement each operation in O(1) time complexity.

import unittest
from typing import List

class Node:
    def __init__(self, value):
      self.value = value
      self.next = None
      self.prev = None

class Deque:
    def __init__(self):
        # Create two dummy nodes and link them
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value

# Example 1 
#   Input:
#   ["isEmpty", "append", 10, "isEmpty", "appendLeft", 20, "popLeft", "pop", "pop", "append", 30, "pop", "isEmpty"]
#   Output:
#   [true, null, false, null, 20, 10, -1, null, 30, true]

class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_isEmpty(self):
        self.assertTrue(self.deque.isEmpty())
        self.deque.append(10)
        self.assertFalse(self.deque.isEmpty())

    def test_append_and_pop(self):
        self.deque.append(10)
        self.assertEqual(self.deque.pop(), 10)
        self.assertTrue(self.deque.isEmpty())

    def test_appendleft_and_popleft(self):
        self.deque.appendleft(20)
        self.assertEqual(self.deque.popleft(), 20)
        self.assertTrue(self.deque.isEmpty())

    def test_scenario_example_1(self):
        commands = ["isEmpty", "append", 10, "isEmpty", "appendleft", 20, "popleft", "pop", "pop", "append", 30, "pop", "isEmpty"]
        expected_output = [True, None, False, None, 20, 10, -1, None, 30, True]

        output = []
        idx = 0
        while idx < len(commands):
            command = commands[idx]
            if command == "isEmpty":
                output.append(self.deque.isEmpty())
            elif command == "append":
                idx += 1
                self.deque.append(commands[idx])
                output.append(None)
            elif command == "appendleft":
                idx += 1
                self.deque.appendleft(commands[idx])
                output.append(None)
            elif command == "pop":
                output.append(self.deque.pop())
            elif command == "popleft":
                output.append(self.deque.popleft())
            idx += 1

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
