from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = Counter(nums)
        output =[]
        appearance = n/3
        for num in nums:
            if count[num] > appearance:
                output.append(num)
                count[num] = 0
        return output

        
