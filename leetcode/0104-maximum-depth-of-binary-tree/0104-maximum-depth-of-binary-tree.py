# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l,r)
        

        # l = r = 1
        # def dfs(node):
        #     if node:
        #         dfs(node.left)
        #         l += 1
        #         dfs(node.right)
        #         r += 1     
        # dfs(root)
        # return max(l,r)

