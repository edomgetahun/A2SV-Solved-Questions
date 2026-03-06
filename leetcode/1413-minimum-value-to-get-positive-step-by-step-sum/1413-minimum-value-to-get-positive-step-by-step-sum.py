class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = 0
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            curr += nums[i]
            prefix[i] = curr

        minval = min(prefix)
        if minval <= 0:
            return 1 - minval
        else:
            return 1
