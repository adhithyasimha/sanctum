# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        seen=set()
        while curr:
            if curr.val in seen:
                prev.next=curr.next
                curr=curr.next
            else:
                seen.add(curr.val)
                prev=curr
                curr=curr.next
        return dummy.next
                




