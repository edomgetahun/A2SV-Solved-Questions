class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        def checker(mid):
            put = 1
            prev = pos[0] # when we start we assume the first ball is put at the first index and we try to find the next valid place
            for i in range(1, len(pos)):
                if pos[i] - prev >= mid:
                    put += 1
                    prev = pos[i]

            if put >= m:
                return True
            return False
        
        l ,r = 0,  max(pos) - min(pos)
        ans = 0
        while l <= r:
            mid = (l+r)//2  # mid is the candidate diff i can get
            if checker(mid) == True:
                ans = mid 
                l = mid + 1
            else:
                r = mid - 1
        return ans
        


        
        
        
       




