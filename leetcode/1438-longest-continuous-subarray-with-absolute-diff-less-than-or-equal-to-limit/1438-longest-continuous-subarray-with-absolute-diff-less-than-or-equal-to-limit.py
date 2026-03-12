class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = deque()
        inc = deque()
        max_len = 0
        l = 0
        for r in range(len(nums)):
            while dec and nums[dec[-1]] < nums[r]:
                dec.pop()
            dec.append(r)

            while inc and nums[inc[-1]] > nums[r]:
                inc.pop()
            inc.append(r)

            while nums[dec[0]] - nums[inc[0]] > limit:
                if dec[0] == l: 
                    dec.popleft() 
                if inc[0] == l: 
                    inc.popleft() 
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
        

       
       



