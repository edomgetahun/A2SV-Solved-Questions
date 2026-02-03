class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_str = str(x)
        reversed_str = x_str[::-1]
        return x_str == reversed_str
