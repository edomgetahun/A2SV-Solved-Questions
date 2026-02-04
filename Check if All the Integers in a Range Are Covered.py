class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        [[1,2],[,4]]
        """
        ranges.sort()
        for num in range(left, right+1):
            l = 0
            found = False
            while l < len(ranges):
                if ranges[l][0] <= num <= ranges[l][1]:
                    found = True
                    break
                else:
                    l += 1
            if found == False:
                return False  
        return True

        # ranges.sort()
        # res = []
        # n = len(ranges)
        # l = 0 
        # r = l + 1
        # while l < n:
        #     while r < n and ranges[r][0] == ranges[l][1]+ 1:
        #         ranges[l][1] = max(ranges[l][1], ranges[r][1])
        #         r += 1
        #     res.append(ranges[l])
        #     l = r
        #     r += 1
        # for i in range(len(res)):
        #     if res[i][0] <= left <= right <= res[i][1]:
        #         return True
        #     else:
        #         return False




            
          
               
                    









        
