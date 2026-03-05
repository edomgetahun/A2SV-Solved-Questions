class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        total = 1
        temp = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                temp *= nums[i]

            total *= nums[i]
        
        
        output = []
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(temp)
            else:
                output.append(total // nums[i])
        return output






        
        
        


        

        