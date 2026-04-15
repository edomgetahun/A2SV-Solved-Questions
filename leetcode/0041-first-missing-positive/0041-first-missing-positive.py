class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = max(nums)
        nums = set(nums)
        for num in range(1, end+2):
            if num not in nums:
                return num
        return 1