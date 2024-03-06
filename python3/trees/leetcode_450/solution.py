# 450
# https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        # Input: root = [5,3,6,2,4,null,7], key = 3
        # Output: [5,4,6,2,null,null,7]
        #      5
        #   3    6 
        # 2  4     7

        # root.left
        # root.val
        # root.right

        # base case if tree is empty
        if not root: return None
            
        # search for node to remove
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        else: 
            if not root.left:  # Node has no left child or only right child
                return root.right
            elif not root.right:  # Node has only left child
                return root.left
            else:  # Node has both left and right children
                # Find the inorder successor (minimum node in right subtree)
                successor = root.right
                while successor.left:
                    successor = successor.left

                # Replace root value with the successor value
                root.val = successor.val

                # Delete the successor from the right subtree
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
