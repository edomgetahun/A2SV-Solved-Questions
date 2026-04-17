class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(indx, prev):
            if indx == len(s):
                return True
            for j in range(indx,len(s)):
                val = int(s[indx:j+1])
                if val + 1 == prev:
                    if dfs(j+1, val):
                        return True
            return False
        for i in range(len(s)-1):
            val =  int(s[:i+1])
            if dfs(i+1, val):
                return True
        return False