class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        mid = num // 3
        a = mid -1
        c = mid + 1
        output = []
        if a + mid + c ==  num :
            output.append(a)
            output.append(mid)
            output.append(c)
            return output
        else:
            return []

        
