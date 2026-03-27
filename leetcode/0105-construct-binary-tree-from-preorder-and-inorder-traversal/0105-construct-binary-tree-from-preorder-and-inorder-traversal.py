# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        count = defaultdict(int)
        for i,val in enumerate(inorder):
            count[val] = i
        self.temp =  0
        def helper(i,j):
            if i > j:
                return 
            
            root = TreeNode(preorder[self.temp])
            self.temp += 1

            left_sub = helper(i, count[root.val]-1)
            root.left = left_sub
            right_sub = helper(count[root.val] + 1, j)
            root.right = right_sub

            return root
        return helper(0, len(preorder)-1) 

