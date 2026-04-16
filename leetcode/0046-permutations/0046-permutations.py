class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bk(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            for i in range(len(nums)):
                if nums[i] in comb:
                    continue
                comb.append(nums[i])
                bk(comb)
                comb.pop()
        bk([])
        return res









        # res = []
        # def backtrack(curr):
        #     if len(curr) == len(nums):
        #         res.append(curr[:])
        #         return
        #     for num in nums:
        #         if num not in curr:
        #             curr.append(num)
        #             backtrack(curr)
        #             curr.pop()
                
        # backtrack([])
        # return res
