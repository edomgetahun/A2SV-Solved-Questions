# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def dfs(l, r , nums):
            if l >= r:
                return
            maxx = l
            for i in range(l,r):
                if nums[i] > nums[maxx]:
                    maxx = i
            node = TreeNode(nums[maxx])
            node.left = dfs(l, maxx, nums)
            node.right = dfs(maxx+1, r, nums)
            return node  
        return dfs(0, n, nums)
        
    

        