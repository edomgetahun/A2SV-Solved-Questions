class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # option 1
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for num in range(start, n+1):
                comb.append(num)
                backtrack(num + 1, comb)
                comb.pop()

        res = []
        backtrack(1, [])
        return res


            # option 2
        # def backtrack(num, comb):
        #     if len(comb) == k:
        #         res.append(comb[:])
        #         return
        #     if num > n:
        #         return
        #     comb.append(num)
        #     backtrack(num+1, comb)
        #     comb.pop()
        #     backtrack(num+1, comb)
        
        # res = []
        # backtrack(1, [])
        # return res
