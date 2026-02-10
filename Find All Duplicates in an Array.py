from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        output = []
        for num in nums:
            if count[num] >= 2:
                output.append(num)
                count[num] = 0
        return output
            
         
        
