# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(node):
            prev=None
            curr=node
            while curr:
                nextnode=curr.next
                curr.next=prev
                prev=curr
                curr=nextnode
            return prev
        head=reverse(head)

        dummy=ListNode(0,head)
        curr=dummy
        i=0
        while curr:
            if i==n-1:
                curr.next=curr.next.next
                break
            curr=curr.next
            i+=1
        return reverse(dummy.next)
        


        