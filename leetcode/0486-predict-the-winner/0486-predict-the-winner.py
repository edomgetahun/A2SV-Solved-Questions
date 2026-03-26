class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(left, right):
            if left == right:
                return nums[left]

            op1 = nums[left] - dfs(left + 1, right)     
            op2 = nums[right] - dfs(left, right -1)
            return max(op1, op2)
        if dfs(0, len(nums)-1) >= 0:
            return True
        return False
