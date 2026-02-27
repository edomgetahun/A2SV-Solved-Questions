class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = Counter()
        l = 0
        length = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while (r-l+1) - count[1] > 1:
                count[nums[l]] -= 1
                l += 1
            length = max(length, r -l +1)
        
        return length-1
