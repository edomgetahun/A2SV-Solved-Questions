class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        checker = ['b','a','l','o','n']
        checker = set(checker)
        for ch in text:
            if ch in checker:
                count[ch] += 1
        count['l'] //= 2
        count['o'] //= 2
        cnt = len(count)
        if cnt < 5:
            return 0
        return min(count.values())
           
                
