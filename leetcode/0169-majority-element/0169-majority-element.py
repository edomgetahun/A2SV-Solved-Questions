class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        temp = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for key in temp:
            return key