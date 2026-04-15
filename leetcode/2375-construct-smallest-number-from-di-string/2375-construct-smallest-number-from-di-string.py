class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, used = [], set()
        def bk(path):
            if res:
                return
            if len(path) == len(pattern) + 1:
                res.append("".join(path))
                return
            for num in range(1, 10):
                if num in used:
                    continue 
                
                if path: 
                    indx = len(path) - 1
                    prev = int(path[-1])
                    if pattern[indx] == "I" and num <= prev:
                        continue
                    else:
                        if pattern[indx] == "D" and num >= prev:
                            continue
                used.add(num)
                path.append(str(num))
                bk(path)
                path.pop()
                used.remove(num)
        bk([])
        return res[0]
       