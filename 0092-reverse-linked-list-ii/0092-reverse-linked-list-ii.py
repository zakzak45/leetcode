# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        dummyNode = ListNode(None)
        leftPrev = dummyNode
        dummyNode.next = head
        for i in range(left-1):
            leftPrev = leftPrev.next
        curr = leftPrev.next
        prev = None
        
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummyNode.next
        