class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            temp =[]
            while num > 0:
                r = num % 10 
                num = num // 10
                temp.append(r)
            temp.reverse()
            output += temp
        return output
