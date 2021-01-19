# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  
        result = ListNode()
        head = result
        while True:
            mi = 10001
            flag = 1
            for i in range(len(lists)):
                if lists[i] == None:
                    pass
                elif mi > lists[i].val:
                    mi = lists[i].val
                    temp = i
                    flag = 0
            if flag == 1:
                break
            
            result.next = ListNode()
            result = result.next
            result.val = mi
            lists[temp] = lists[temp].next
            
        return head.next