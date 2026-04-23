class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0
        for i in range(len(nums) - 1):
            maxx = max(maxx, nums[i+1] - nums[i])
        return maxx