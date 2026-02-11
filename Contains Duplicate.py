from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = Counter(nums)
        for key in counts:
            if counts[key] > 1:
                return True
        return False
