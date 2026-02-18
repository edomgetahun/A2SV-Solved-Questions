class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        lcount = Counter()
        rcount = Counter(nums)
        for i in range(len(nums)):
            lcount[nums[i]] += 1
            rcount[nums[i]] -= 1
            len_l = i + 1
            len_r = len(nums) - i - 1

            if lcount[nums[i]] * 2 > len_l and len_r < rcount[nums[i]] * 2 :
                return i
        return -1



