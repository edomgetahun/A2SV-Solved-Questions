class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atmost(goal):
            curr = 0
            l = 0
            cnt = 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > goal and l <= r:
                    curr -= nums[l]
                    l += 1
                cnt += r-l+1
            return cnt
        return atmost(goal) - atmost(goal-1)