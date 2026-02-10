class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen ={}
        for i, v in enumerate(nums):
            complement = target- nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i 



                    
        
        

      
  
