class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = {0:1} # key = current running sum , value:- the freq of that prefix sum exist
        curr = 0
        cnt = 0
        for num in nums:
            curr += num
            x = curr - k
            if x in count:
                cnt += count[x]
            count[curr] = 1 + count.get(curr, 0)
        return cnt
                

            

            
       
        
            



