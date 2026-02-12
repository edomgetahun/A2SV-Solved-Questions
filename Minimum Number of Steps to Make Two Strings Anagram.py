class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS = Counter(s)
        counterT = Counter(t)

        steps = 0
        for ch in counterT:
            if ch in counterS:
                if counterT[ch] > counterS[ch]:
                    steps += counterT[ch] - counterS[ch]
            else:
                steps += counterT[ch]

        return steps
