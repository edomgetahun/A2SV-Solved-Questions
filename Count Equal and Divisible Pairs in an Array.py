class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if max(count.values()) == 1:
            return 0
        
        mydict = defaultdict(list)
        for i, v in enumerate(nums):
            mydict[v].append(i)
        
        pair = 0
        for val in mydict.values():
            for i in range(len(val)):
                for j in range(i+1, len(val)):
                    if val[i]*val[j] % k == 0:
                        pair += 1
        return pair

        
