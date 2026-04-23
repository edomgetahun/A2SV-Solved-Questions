class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        minn, maxx = 0, 2
        key , i = 0 , 0
        while key <= maxx:
            while count[key] > 0:
                nums[i] = key
                count[key] -= 1
                i += 1
            key += 1
            

