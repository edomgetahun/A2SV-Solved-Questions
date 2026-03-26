# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = {0: 1} 
        def dfs(node, run):
            if node is None:
                return 0

            run += node.val
            needed_sum = run - targetSum
            total_paths = count.get(needed_sum, 0)
            if run in count:
                count[run] += 1
            else:
                count[run] = 1
            total_paths += dfs(node.left, run)
            total_paths += dfs(node.right, run)
            count[run] -= 1
            return total_paths
        return dfs(root, 0)