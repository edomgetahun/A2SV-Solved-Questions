class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()
        l ,r = 1,max(candies)
        ans = 0
        while l <= r:
            mid = (l+r) // 2
            run = 0
            for c in candies:
                run += c//mid
            if run >= k:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
            
