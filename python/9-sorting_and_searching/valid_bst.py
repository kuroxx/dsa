from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # inorder traversal of bst (ascending order)
    prev: TreeNode = None
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not self.is_valid_bst(root.left): return False
        if self.prev and self.prev.val >= root.val: return False
        self.prev = root
        return self.is_valid_bst(root.right)