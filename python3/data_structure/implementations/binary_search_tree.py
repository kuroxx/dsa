# https://neetcode.io/problems/binarySearchTree

# Design a Binary Search Tree class.

# Note:
# The tree should be ordered by the keys.
# The tree should not contain duplicate keys. 
# If the key is already present in the tree, the original key-val pair should be overridden with the new key-value pair.

import unittest
from typing import List

class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True: # because 1 of 3 use cases will definitely execute
            if key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            elif key < curr.key: 
                if not curr.left: 
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else: 
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.findMin(self.root)
        return curr.val if curr else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Remove the node with key, return the new root of the subtree
    def removeHelper(self, curr, key) -> TreeNode:
        if curr == None: 
            return None
        
        if key > curr.key: 
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                # swap curr node with inorder successor (smallest in right subtree)
                min_node = self.findMin(curr.right)
                curr.key = min_node.key
                curr.val = min_node.val
                # remove the node
                curr.right = self.removeHelper(curr.right, min_node.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = [] 
        self.inorderTraversal(self.root, result)
        return result


    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None: 
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)


# Example 1 
#   Input:
#   ["insert", 1, 2, "get", 1, "insert", 4, 0, "getMin", "getMax"]
#   Output:
#   [null, 2, null, 2, 0]

# Example 2 
#   Input:
#   ["insert", 1, 2, "insert", 4, 2, "insert", 3, 7, "insert", 2, 1, "getInorderKeys", "remove", 1, "getInorderKeys"]
#   Output:
#   [null, null, null, null, [1, 2, 3, 4], null, [2, 3, 4]]


class TestTreeMap(unittest.TestCase):
    def setUp(self):
        self.tree_map = TreeMap()

    def test_example_1(self):
        commands = ["insert", 1, 2, "get", 1, "insert", 4, 0, "getMin", "getMax"]
        expected_output = [2, 2, 0]

        output = []
        idx = 0
        while idx < len(commands):
            command = commands[idx]
            if command == "insert":
                idx += 1
                self.tree_map.insert(commands[idx], commands[idx + 1])
                idx += 1
            elif command == "get":
                idx += 1
                output.append(self.tree_map.get(commands[idx]))
            elif command == "getMin":
                output.append(self.tree_map.getMin())
            elif command == "getMax":
                output.append(self.tree_map.getMax())
            idx += 1

        self.assertEqual(output, expected_output)

    def test_example_2(self):
        commands = ["insert", 1, 2, "insert", 4, 2, "insert", 3, 7, "insert", 2, 1, "getInorderKeys", "remove", 1, "getInorderKeys"]
        expected_output = [[1, 2, 3, 4], [2, 3, 4]]

        output = []
        idx = 0
        while idx < len(commands):
            command = commands[idx]
            if command == "insert":
                idx += 1
                self.tree_map.insert(commands[idx], commands[idx + 1])
                idx += 1
            elif command == "getInorderKeys":
                output.append(self.tree_map.getInorderKeys())
            elif command == "remove":
                idx += 1
                self.tree_map.remove(commands[idx])
            idx += 1

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
