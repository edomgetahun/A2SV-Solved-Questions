class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        total = skill[l] + skill[r]
        ans = 0
        while l < r:
            if skill[l] + skill[r] == total:
                ans += (skill[l] * skill[r])
                l += 1
                r -= 1  
            else:
                return -1
        return ans



        
