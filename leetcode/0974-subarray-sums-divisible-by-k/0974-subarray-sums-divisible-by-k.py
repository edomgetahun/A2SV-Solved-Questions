class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        res = 0
        count = defaultdict(int)
        count[0] = 1
        for num in nums:
            prefix += num
            rem = prefix % k 
    
            res += count[rem] 
            count[rem] += 1
        return res