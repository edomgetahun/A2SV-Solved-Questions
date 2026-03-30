# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        post_indx = {}
        for i, num in enumerate(postorder):
            post_indx[num] = i
        
        def helper(i1, i2, j1, j2): # tells which portion for preorder then post order look at it
            if i1 > i2 or j1 > j2:  # if these pointer crosses empty tree
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:    # we should have to create another node 
                left_val = preorder[i1+1]
                mid = post_indx[left_val]
                left_size = mid - j1 + 1
                
                root.left = helper(i1+1, i1 + left_size  ,j1, mid)
                root.right = helper( i1 + left_size +1, i2,  mid+1, j2 -1) #  i1 + left_size  :- where the left part ends in the preorder and j2 -1 := exclude the root

            return root
        return helper(0,n-1, 0, n-1)
