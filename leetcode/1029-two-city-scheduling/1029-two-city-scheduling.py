class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        costs.sort(key = lambda x: x[0] - x[1])
        print(costs)
        i = 0
        while i < len(costs):
            if i < len(costs)//2:
                total += costs[i][0]
                i += 1
            else:
                total += costs[i][1]
                i += 1
        return total
            
            
        