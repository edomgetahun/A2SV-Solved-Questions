"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mydict = {}
        for emp in employees:
            mydict[emp.id] = emp
        
        q = deque([id])
        total = 0
        while q:
            cur_id = q.popleft()
            employe = mydict[cur_id]
            total += employe.importance
            for sub_id in employe.subordinates:
                q.append(sub_id)
        return total


        
