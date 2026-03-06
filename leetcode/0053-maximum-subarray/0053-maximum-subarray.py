class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_sum = nums[0]
        curr = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            max_sub_sum = max(max_sub_sum, curr)
        return max_sub_sum