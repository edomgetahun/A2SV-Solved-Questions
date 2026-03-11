class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        count = Counter()
        
        for i in range(n-1 , -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                count[nums2[i]] = -1
            else:
                count[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        output = []
        for num in nums1:
            output.append(count[num])
        return output

          

