class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bk(start, comb):
            if len(comb) >= 2:
                res.append(comb[:])
            
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] not in seen:
                    if comb and nums[i] < comb[-1]:
                        continue 
                    seen.add(nums[i])
                    comb.append(nums[i])
                    bk(i+1, comb)
                    comb.pop()
        bk(0, [])
        return res