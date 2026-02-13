class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRN = Counter(ransomNote)
        countM = Counter(magazine)
        
        found = False
        for ch in countRN:
            if countRN[ch] <= countM[ch]:
                found = True
                continue
            else:
                found = False
                break
        
        if found:
            return True
        else:
            return False
            



            
