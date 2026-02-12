class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        res = sum(x for x in nums if x % 2 == 0)
        output = []
        for i in range(len(queries)):
            val = queries[i][0]
            indx = queries[i][1]

            if nums[indx] % 2 == 0:
                res -= nums[indx]
            nums[indx] += val

            if nums[indx] % 2 == 0:
                res += nums[indx]

            output.append(res)

        return output
