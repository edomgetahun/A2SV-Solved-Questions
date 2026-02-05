class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        count = float('inf')
        for s in list2:
            if s in list1:
                i = list1.index(s)
                j = list2.index(s)
                count = min(count, i+j)
        for s in list2:
            if s in list1:
                i = list1.index(s)
                j = list2.index(s)
                if count == i+j:
                    res.append(s)
        return res


            







        
