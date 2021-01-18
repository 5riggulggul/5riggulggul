# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        head = temp
        while True:
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                temp.next = l2
                temp = temp.next
                temp.val = l2.val
                l2 = l2.next
            elif l2 == None:
                temp.next = l1
                temp = temp.next
                temp.val = l1.val
                l1 = l1.next
            else:
                if l1.val >= l2.val:
                    temp.next = l2
                    temp = temp.next
                    temp.val = l2.val
                    l2 = l2.next
                elif l1.val < l2.val:
                    temp.next = l1
                    temp = temp.next
                    temp.val = l1.val
                    l1 = l1.next
        return head.next