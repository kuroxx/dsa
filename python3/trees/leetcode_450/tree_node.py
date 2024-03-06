# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BuildTreeNode:
    def build(self, elements: list):
        if elements == []:
            return None

        queue = collections.deque(elements)
        root_val = queue.popleft()
        root_node = TreeNode(root_val)
        
        root_queue = collections.deque()
        root_queue.append(root_node)
        left_val = None
        right_val = None
        while queue:
            left_val = queue.popleft()
            if queue:
                right_val = queue.popleft()
    
            root_to_be_linked = root_queue.popleft()

            if left_val:
                left_node = TreeNode(left_val)
                left_val = None
                root_queue.append(left_node)
                root_to_be_linked.left = left_node
            
            if right_val:
                right_node = TreeNode(right_val)
                right_val = None
                root_queue.append(right_node)
                root_to_be_linked.right = right_node
        return root_node
    
    def tree_to_array(self, tree):
        res = []
        que = collections.deque()
        que.append(tree)
        while que:
            que_len = len(que)
            for _ in range(que_len):
                node = que.popleft()
                val = node.val if node else None
                res.append(val)
                if node:
                    que.append(node.left)
                    que.append(node.right)
        for i in range(len(res)-1, -1, -1):
            if res[i] is None:
                res.pop()
            else:
                break
        
        return res