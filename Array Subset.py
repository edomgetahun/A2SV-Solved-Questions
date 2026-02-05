#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
            count1= Counter(a)
            count2= Counter(b)
            for num in b :
                if count2[num] > count1[num]:
                    return False
            return True

            
            
                
            
                        
                    
                
                
            
            
    
    
    
    
