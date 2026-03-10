class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent = {")": "(", "]": "[" , "}" :"{" }  
        for i in range(len(s)):
            if s[i] not in parent:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if a != parent[s[i]]:
                        return False
        return True if not stack else False