# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node,val):
            if not node:
                return TreeNode(val)
            if val >node.val:
                node.right=helper(node.right,val)
            elif val < node.val:
                node.left=helper(node.left,val)
            return node
        root=helper(root,val)
        return root
        