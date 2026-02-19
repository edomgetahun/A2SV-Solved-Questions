class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_list = sorted(nums)
        count = {}
        for index, value in enumerate(sorted_list):
            if value not in count:
                count[value] = index
        result  = []
        for value in nums:
            result.append(count[value])
        return result


