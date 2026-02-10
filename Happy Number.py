class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        my_set = set()
        while n!=1 and n not in my_set:
            my_set.add(n)
            total = 0
            while n > 0 :
                digit = n % 10
                total += digit * digit 
                n //= 10
            n = total
        if n == 1:
            return True
        else:
            return False


        
