class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        for num in count:
            if count[num] == 2:
                res.append(num)
        for num in range(1, len(nums)+1):
            if num not in nums:
                res.append(num)
        return res


