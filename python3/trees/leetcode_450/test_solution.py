import unittest
from solution import Solution
from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_deleteNode(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([5,3,6,2,4,None,7])
        key = 3
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [5,4,6,2,None,None,7])

        tree = builder.build([5,3,6,2,4,None,7])
        key = 0
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [5,3,6,2,4,None,7])

        tree = builder.build([])
        key = 0
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [])

if __name__ == "__main__":
    unittest.main()
