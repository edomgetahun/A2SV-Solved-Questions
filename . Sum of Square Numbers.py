class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0       # smallest value
        b =  int(math.sqrt(c)) # largest possible value
        while a <= b:
            curr = a*a + b*b
            if curr == c:
                return True
            elif curr < c:
                a += 1
            else:
                b -= 1
        return False

        
