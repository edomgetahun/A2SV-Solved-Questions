class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []
        for ch in order:
            while count[ch] >= 1:
                res.append(ch)
                count[ch] -= 1
        s = set(s)
        for ch in s:
            if ch not in order:
                while count[ch] >= 1:
                    res.append(ch)
                    count[ch] -= 1
        return "".join(res)
        
        
