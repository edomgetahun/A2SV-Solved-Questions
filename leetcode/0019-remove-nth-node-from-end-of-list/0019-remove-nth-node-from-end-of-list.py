# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # cnt = 0
        # temp = head
        # while temp:
        #     cnt += 1
        #     temp = temp.next
        
        # pos = 1
        # temp = head
        # while temp :
        #     if pos == n - k:



        #     else:
        #         temp = tem.next
        #         pos += 1

        dummy = ListNode(None)
        dummy.next = head
        l = dummy
        r = dummy
        cnt = 0
        while r :
            if cnt < n+1:
                r = r.next
            else:   
                r = r.next
                l = l.next
            cnt += 1
        l.next = l.next.next
        return dummy.next  

        

       

