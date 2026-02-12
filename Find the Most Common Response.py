class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        count = Counter()
        for day in responses:
            day = set(day)
            for s in day:
                count[s] += 1

        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        max_val = max(sorted_count.values())
        
        output = []
        for key in sorted_count:
            if sorted_count[key] == max_val:
                output.append(key)
        
        output.sort()
        return output[0]

        


        

            
