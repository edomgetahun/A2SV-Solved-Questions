class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayatmostk(k):
            cnt = 0
            l = 0
            count = {}
            for r in range(len(nums)):
                count[nums[r]] = count.get(nums[r], 0) + 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]] 
                    l += 1
                cnt += r -l + 1
            return cnt
        return subarrayatmostk(k) - subarrayatmostk(k -1)
            


          
          


