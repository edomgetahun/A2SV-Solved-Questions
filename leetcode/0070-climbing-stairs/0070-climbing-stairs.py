class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(i):
            if i < 3:
                return i
            if i not in memo:
                memo[i] = solve(i-1) + solve(i-2)
            return memo[i]
        return solve(n)
        