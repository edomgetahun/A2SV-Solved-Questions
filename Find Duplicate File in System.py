class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        for path in paths:
            word = path.split()
            root = word[0]
            for i in range(1, len(word)):
                temp = word[i].split("(")
                key = temp[1][:-1]
                value = root + "/" + temp[0]
                if key not in mydict:
                    mydict[key] = [value]
                else:
                     mydict[key].append(value)
        output =[]
        for value in mydict.values():
            if len(value) <= 1:
                continue
            else:
                output.append(value)
        return output



                
