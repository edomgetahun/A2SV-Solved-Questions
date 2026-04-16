class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def bk(start, comb):
            if len(comb) >= 2:
                res.add(tuple(comb[:]))
                
            for i in range(start, len(nums)):
                if comb and comb[-1] > nums[i]:
                    continue
                comb.append(nums[i])
                bk(i+1, comb)
                comb.pop()
        bk(0, [])
        return list(res)

