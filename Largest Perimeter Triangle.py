class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            c = nums[i]
            b = nums[i-1]
            a = nums[i-2]
            if a+b > c:
                per = a+b+c
                return per
        else:
            return 0






        
        
                



      

        
