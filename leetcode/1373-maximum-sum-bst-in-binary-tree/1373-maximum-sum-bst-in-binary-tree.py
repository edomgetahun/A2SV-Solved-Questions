# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node: # true, min, max, sum=0
                return True, float('inf'), float("-inf"), 0

            l_isBST, l_min, l_max, l_sum = dfs(node.left)
            r_isBST, r_min, r_max, r_sum= dfs(node.right)
            if l_isBST and r_isBST and l_max < node.val < r_min:
                cur_sum = l_sum + r_sum + node.val
                self.ans = max(self.ans, cur_sum)
                min_val = min(l_min, node.val)
                max_val = max(r_max, node.val)
                return True, min_val, max_val, cur_sum
            return False, 0, 0, 0
        dfs(root)
        return self.ans
