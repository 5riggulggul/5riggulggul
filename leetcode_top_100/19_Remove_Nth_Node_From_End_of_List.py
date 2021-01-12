class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temphead = head
        if not temphead.next and n == 1:
            return 
        while temphead.next:
            head2 = temphead
            flag = 0
            for i in range(n):
                head2 = head2.next
                if i == n-1 and head2 is None:
                    head = temphead.next
                    flag = 1
                elif i == n-1 and not head2.next:
                    temphead2 = temphead.next
                    temphead.next = temphead2.next
                    flag = 1
                
            if flag == 1:
                break
            temphead = temphead.next
        return head