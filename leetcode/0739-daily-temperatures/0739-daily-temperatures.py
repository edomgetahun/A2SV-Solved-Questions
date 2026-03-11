class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        count = [0] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temp[i]:
                stack.pop()
            if stack:
                ans = stack[-1][1] - i
                count[i] = ans     
            stack.append((temp[i], i)) 
        return count
        
