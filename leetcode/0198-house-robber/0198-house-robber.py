class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if memo[i] == -1:
                memo[i] = max(rob(i-1), rob(i-2)+nums[i])
            return memo[i]
        memo = [-1 for _ in range(len(nums))]
        return rob(len(nums)-1)