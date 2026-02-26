class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = set()
        res = []
        count = {}
        r = len(s) - 1
        for l in range(len(s)):
            if s[l] not in seen:
                while s[l] != s[r] and r >= 0:
                    r -= 1
                count[s[l]] = r
                r = len(s) - 1 
        
        start = 0
        curr = count[s[0]]
        for i in range(len(s)):
            if count[s[i]] > curr:
                curr = count[s[i]]
            if i == curr:   
                size = i - start + 1
                res.append(size)
                start = i + 1  
        return res
        
