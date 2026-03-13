# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while  temp:
            while stack and temp.val > stack[-1]:
                stack.pop()
            stack.append(temp.val)
            temp = temp.next
        
        dummy = ListNode(-1)
        curr = dummy
        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

            

        
