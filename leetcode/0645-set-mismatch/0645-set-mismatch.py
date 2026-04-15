class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        count = Counter(nums)
        for num in count:
            if count[num] == 2:
                dup = num
                res.append(dup)

        expeted = (n*(n +1))//2
        curr = sum(nums)
        mis = expeted - (curr - dup)
        res.append(mis)
        return res
        

