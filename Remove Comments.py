class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_comment = False
        ans = []
        cur = ""
        for word in source:
            i = 0
            while i < len(word):
                if word[i: i+2] == "/*" and not in_comment:
                    in_comment = True
                    i += 2
                elif word[i: i+2] == "*/" and in_comment:
                    in_comment = False
                    i += 2
                elif word[i: i+2] == "//" and not in_comment:
                    break 
                else:
                    if in_comment == False:
                        cur += word[i]
                    i += 1
            if cur != "" and not in_comment:
                ans.append(cur)
                cur = ""
        return ans
