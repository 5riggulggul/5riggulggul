# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        interval = 1
        while interval < len(lists): # 전체 길이보다 interval이 커질 때 동작 그만
            for i in range(0,len(lists)-interval,interval*2): # divide and conquer이기 때문에 interval*2의 step
                lists[i] = self.merge2lists(lists[i], lists[i+interval]) # self를 붙여야 한다.(클래스 내 자신의 함수 호출이기 때문에)
            interval *= 2 # interval을 2배 해주어 다음 병합 수행
        if len(lists) == 0: # 비어있는 lists 처리
            return
        else:
            return lists[0]
        
    def merge2lists(self, l1, l2): #두 ListNode 합치는 함수
        head = temp = ListNode()
        while l1 or l2:
            temp.next = ListNode()
            temp = temp.next
            if not l1:
                temp.val = l2.val
                l2 = l2.next
            elif not l2:
                temp.val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                temp.val = l1.val
                l1 = l1.next
            else:
                temp.val = l2.val
                l2 = l2.next
        return head.next
    
