class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n-1 not in num_set:
                length = 1
                current = n
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
