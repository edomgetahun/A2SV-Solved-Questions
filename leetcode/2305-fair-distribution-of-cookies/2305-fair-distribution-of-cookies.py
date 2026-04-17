class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.res = float('inf')
        def bk(i):
            if i == len(cookies): 
                self.res = min(self.res, max(child)) 
                return
            if max(child) >= self.res: 
                return
            for j in range(k):
                child[j] += cookies[i]
                bk(i+1)
                child[j] -= cookies[i]
        bk(0)
        return self.res
           