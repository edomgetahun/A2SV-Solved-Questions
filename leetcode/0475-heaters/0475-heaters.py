class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        min_rad = float('-inf')

        def find_closest(heaters, house):
            min_dis = float('inf')
            l , r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                min_dis = min(min_dis, abs(heaters[mid] - house))
                if heaters[mid] > house:
                    r = mid - 1
                else:
                    l = mid + 1
            return min_dis
         
        for house in houses:
            min_rad = max(min_rad, find_closest(heaters, house)) 
        return min_rad
    
