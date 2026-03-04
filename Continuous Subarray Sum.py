class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = {0: -1} 
        total = 0
        for i, val in enumerate(nums):
            total += val
            rem = total % k
            if rem not in  count:
                count[rem] = i
            elif i - count[rem] > 1:
                return True
        return False

