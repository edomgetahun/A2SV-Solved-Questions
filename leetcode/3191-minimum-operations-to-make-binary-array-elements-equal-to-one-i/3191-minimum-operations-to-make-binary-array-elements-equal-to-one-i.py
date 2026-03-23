class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cost = 0
        i = 0
        while i < len(nums)-2:
            if nums[i] == 1:
                i += 1
            else:
                j = i
                while j <= i+2:
                    if nums[j] == 0:
                        nums[j] = 1
                        j += 1
                    else:
                        nums[j] = 0
                        j += 1
                cost += 1
                i += 1
        if nums.count(0) == 0:
            return cost
        return -1

                    

            
