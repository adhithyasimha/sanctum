# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int: 
        self.q=[]
        def traversal(node):
            if not node:
                return 
            if node.left and not node.left.left and not node.left.right:
                self.q.append(node.left.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return sum(self.q)
            
        