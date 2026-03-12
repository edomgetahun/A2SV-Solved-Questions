class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        l = r = 0
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop() 
            queue.append(r)
            if queue[0] < r - k + 1: # drived from window size = r -l + 1
                queue.popleft()
            if r + 1 >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1
        return res
