class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        res = []
        for r in range(1,len(s)):
            if int(s[r]) == count[s[r]]:
                if s[r-1] != s[r] and int(s[r-1]) == count[s[r-1]]:
                    res.append(s[r-1])
                    res.append(s[r])
                    return "".join(res)
        else:
            return ""

                




        
