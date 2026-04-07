class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        l = 0
        r = len(nums1) - 1
        if len(nums1) % 2 == 1:
            mid = (l + r) //  2
            return nums1[mid]
        while l < r:
            l += 1
            r -= 1
        return (nums1[l] + nums1[r]) / 2
