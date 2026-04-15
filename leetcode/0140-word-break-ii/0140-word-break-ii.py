class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        res = [] 
        wordDict = set(wordDict)
               
        def bk(start):   
            if start == len(s):
                res.append(" ".join(ans))
                return 
            for end in range(start+1 ,len(s)+1):
                word = s[start:end]
                if word in wordDict:
                    ans.append(word)
                    bk(end)
                    ans.pop()
        bk(0)
        return res
        