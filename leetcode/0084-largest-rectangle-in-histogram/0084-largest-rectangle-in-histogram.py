class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, indx = stack.pop()
                max_area = max(max_area, (i - indx) * height)
                start = indx
            stack.append((h, start))
        
        n = len(heights)
        for height, indx in stack:
            max_area = max(max_area, (n - indx) * height)
        return max_area
            
            
            
       