# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        temp = dummyNode

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next

        # Attach the remaining nodes
        temp.next = curr1 if curr1 else curr2

        return dummyNode.next
