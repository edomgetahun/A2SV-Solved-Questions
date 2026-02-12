class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        firstCount = Counter(word1)
        secCount= Counter(word2)
        
        if firstCount == secCount:
            return True

        keys1 = set(firstCount.keys())
        keys2 = set(secCount.keys())
        vals2 = list(secCount.values())
        count_vals2 = Counter(vals2)
        
        if keys1 == keys2:
            res1 = 0
            found = False
            for key,val in firstCount.items():
                    if val in count_vals2 and count_vals2[val] >= 1:
                        found = True
                        count_vals2[val] -= 1
                    else:
                        found = False
                        break
            
            if found == True:
                return True
            else:
                return False
        else:
            return False         



        
        
        
        
