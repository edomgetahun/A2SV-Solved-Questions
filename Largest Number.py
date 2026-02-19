class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i, v in enumerate(nums):
            nums[i] = str(v)
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        result = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(result)))



        
