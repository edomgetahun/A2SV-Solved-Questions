class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 != 0:
            return []
        res =[]
        changed.sort()
        count = Counter(changed)
        
        for num in changed:
            if count[num] == 0:
                continue
            double = num *2
            if count[double] == 0:
                return []
            res.append(num)
            count[num] -= 1
            count[double] -= 1
        return res

                
            
        
