# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        
        l = head 
        r = head
        temp = 0
        while temp < cnt//2:
            temp += 1
            r = r.next
        return r
            
            
                
