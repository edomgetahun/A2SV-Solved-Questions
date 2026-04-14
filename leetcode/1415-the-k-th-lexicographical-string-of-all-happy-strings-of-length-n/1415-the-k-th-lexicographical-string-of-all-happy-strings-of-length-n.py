class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ["a", "b", "c"]
        res = []
        def bk(temp):
            if len(temp) == n:
                res.append("".join(temp))
                return 
            for i in range(len(s)):
                if temp and s[i] == temp[-1]:
                    continue
                temp.append(s[i])
                bk(temp)
                temp.pop()
        bk([])
        if k > len(res):
            return ""
        return res[k-1] 
