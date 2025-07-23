# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        if len(values) < 2:
            return -1
        
        return sorted(values)[1]
