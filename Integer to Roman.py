class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mydict = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500: "D", 1000: "M"}
        result =""
        values = [1000, 500, 100, 50, 10, 5, 1]
        while num > 0:
            s = str(num)
            first_digit = int(s[0])
            length = len(s)
            place = 10 ** (length - 1)  
            
            if first_digit == 9:
                result += mydict[place] + mydict[place * 10]
                num -= 9 * place
            elif first_digit == 4:
                result += mydict[place] + mydict[place * 5]
                num -= 4 * place
            else:
                for val in values:
                    if val <= num:
                        result += mydict[val]
                        num -= val
                        break
                        
        return result

