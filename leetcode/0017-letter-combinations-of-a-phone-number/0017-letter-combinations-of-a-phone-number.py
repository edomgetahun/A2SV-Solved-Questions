class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_d = {"2":["a","b", "c"], "3": ["d","e", "f"], "4": ["g","h", "i"], "5" : ["j","k", "l"], "6": ["m","n","o"], "7":[ "p","q","r","s"], "8":[ "t","u","v"], "9":[ "w","x","y","z"]}
        res = []
        def backtrack(i, curr):
            if len(digits) == i:
                res.append(curr)
                return 

            letters = my_d[digits[i]]
            for ch in letters:
                backtrack(i+1, curr + ch)

        if digits:
            backtrack(0, "")
        return res


