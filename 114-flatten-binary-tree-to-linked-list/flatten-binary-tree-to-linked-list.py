# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.q=[]
        def pre(node):
            if not node: return
            self.q.append(node)
            pre(node.left)
            pre(node.right)
        pre(root)
        if self.q:
            self.q.pop(0)
            while self.q:
                root.right=self.q.pop(0)
                root.left=None
                root=root.right

        