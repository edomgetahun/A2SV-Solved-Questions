class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n > 0:   
            res = self.myPow(x, n//2)  
            if n % 2 == 1:
                return  res * res * x
            return res * res
        else:
            res = self.myPow(x, math.ceil(n/2))
            if n % 2 == 1:
                return res * res * 1/x
            return res * res 
        
        