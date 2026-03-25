class Solution:
    res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        # initialy start = 1 and comb = []
        # if len==k res.append(comp) and just return
        # for num in range(start, n+1)
        # comb.append(n)
        # backtrack(num + 1, comb)
        # comb.pop()
        
        def backtrack(num, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            if num > n:
                return
            comb.append(num)
            backtrack(num+1, comb)
            comb.pop()
            backtrack(num+1, comb)
        
        res = []
        backtrack(1, [])
        return res
