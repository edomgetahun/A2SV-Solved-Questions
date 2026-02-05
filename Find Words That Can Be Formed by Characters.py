from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        countC = Counter(chars)
        ans = 0
        for word in words:
            countW = Counter(word)
            for ch in word:
                if countW[ch] > countC[ch]:
                    break
            else:
                ans += len(word)
        return ans



        
