class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[0]
        l = 0
        r = len(nums) - 1 
        ans = nums[0]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < nums[0]:
                ans = min(ans, nums[mid])
                r = mid - 1
            else:
                l = mid + 1
        return ans 


