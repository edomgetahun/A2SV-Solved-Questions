# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
            if root is  None:
                return TreeNode(value)
            def search(node):
                if node:
                    if value > node.val:
                        if node.right:  
                            search(node.right)
                        else:
                            newnode = TreeNode(value)
                            node.right = newnode
                    else:
                        if node.left:
                            search(node.left)
                        else:
                            newnode = TreeNode(value)
                            node.left = newnode
            search(root)
            return root
            