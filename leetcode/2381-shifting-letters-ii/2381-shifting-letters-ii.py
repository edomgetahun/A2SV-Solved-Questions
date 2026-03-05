class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0] * len(s)
        for q in  shifts:
            l,r,shift = q
            if shift == 0:
                temp[l] -= 1
                if r < len(s) - 1:
                    temp[r+1] -= -1
            else:
                temp[l] += 1
                if r != len(s)-1:
                    temp[r+1] += -1
        
        prefix = [0] * len(s)
        total = 0   
        for i in range(len(s)):
            total += temp[i]
            prefix[i] = total
        # print(prefix)
        res = [] 
        for i in range(len(s)):
            val = (ord(s[i]) - ord('a') + prefix[i]) % 26
            res.append(chr(val+ ord('a')))
        return "".join(res)
        










