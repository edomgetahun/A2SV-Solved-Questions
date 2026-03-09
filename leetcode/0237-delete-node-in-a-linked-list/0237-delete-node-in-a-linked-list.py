# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #  the head is not given so just copy and then skip 1 node to remove duplicate
        node.val = node.next.val
        node.next = node.next.next 
        