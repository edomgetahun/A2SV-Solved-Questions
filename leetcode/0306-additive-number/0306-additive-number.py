class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        n = len(nums)
        if n < 3:
            return False
        def bk(a,b,c):
            if c == n:
                return True
            for length in range(1, n-c+1):
                if nums[c] == "0" and length > 1:
                    break 
                
                curr = nums[c: length+c] 
                if int(a) + int(b)  < int(curr):
                    break
                elif int(a) + int(b)  > int(curr):
                    continue
                else:
                    if bk(b, curr,length+c):
                        return True
            return False
    
        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[0] == "0" and i > 0:
                    continue
                if nums[i+1] == "0" and j > i + 1:
                    continue
                a = nums[0:i+1]
                b = nums[i+1: j+1]
                if bk(a, b, j+1):
                    return True 
        return False
                 