class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n % 2 == 0:
            even = odd = n //2
        else:
            even = (n // 2) + 1
            odd = n // 2
        return ((pow(5, even, mod) * pow(4, odd, mod))) % mod
        



        
        # def back(x):

        #     if x == n:
        #         if n %2 == 1:
        #             return 5
        #         return 4
        #     temp  = back(x+1)
        #     return (temp*4)%(10**9 + 7) if x%2 == 0 else (temp *5)%(10**9 + 7)
        # return back(1)