# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=root.val
        def dfs(node):
            if not node:
                return 0
            left=max(dfs(node.left),0)
            right=max(dfs(node.right),0)

            current=node.val+left+right
            self.maxsum=max(self.maxsum,current)

            return node.val+max(left,right)
        dfs(root)
        return self.maxsum