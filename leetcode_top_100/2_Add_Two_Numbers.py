# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        tail = result
        while l1 or l2: # l1!= None or l2!= None 과 같다
            if not l1:
                tail.val += l2.val
                if tail.val == 10:
                    tail.val = 0
                    tail.next = ListNode(1)
                else:
                    tail.next = ListNode(0)
                l2 = l2.next
            elif not l2:
                tail.val += l1.val
                if tail.val == 10:
                    tail.val = 0
                    tail.next = ListNode(1)
                else:
                    tail.next = ListNode(0)
                l1 = l1.next
            elif l1.val + l2.val + tail.val >= 10:
                tail.val += l1.val + l2.val - 10
                tail.next = ListNode(1)
                l1 = l1.next
                l2 = l2.next
            elif l1.val + l2.val + tail.val < 10:
                tail.val += l1.val + l2.val
                tail.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
            if not(l1 or l2 or tail.next.val==1): #tail.next.val==1은 carry존재 의미
                tail.next = None
            else: 
                tail = tail.next
        return result