class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(nums, n, curr):
            left = 2*curr + 1
            right = 2*curr + 2
            maxx = curr
            if left < n and nums[left] > nums[maxx]:
                maxx = left
            if right < n and nums[right] > nums[maxx]:
                maxx = right
            if curr != maxx:
                nums[curr],nums[maxx] = nums[maxx], nums[curr]
                heapify(nums, n, maxx)  
        
        n = len (nums)
        ans = []
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
        ans = None
        for i in range(k):
            ans = nums[0]
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            heapify(nums, n - 1 - i, 0)
        return ans


