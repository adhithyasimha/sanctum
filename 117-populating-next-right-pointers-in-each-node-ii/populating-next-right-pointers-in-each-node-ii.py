"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue=[root]
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                node=queue.pop(0)
                level.append(node.val)
                if i < size-1:
                    node.next=queue[0]
                else:
                    node.next=None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
                

        