class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        output = [""] * len(s)
        for ch, indx in zip(s, indices):
            output[indx] = ch
        return "".join(output)

        
