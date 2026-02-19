class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        cnt = len(piles)//3
        for i in range(len(piles)-1, -1, -2):
            m = piles[i-1]
            if cnt > 0:
                total += m
                cnt -= 1
            else:
                break
        return total

