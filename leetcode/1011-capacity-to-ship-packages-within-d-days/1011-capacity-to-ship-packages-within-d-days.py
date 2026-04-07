class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        def can_ship(capacity):
            num_days = 1
            curr = 0
            for w in weights:
                if curr + w <= capacity:
                    curr += w
                else:
                    curr = w
                    num_days += 1
            if num_days <= days:
                return True
            return False
         
        l = max(weights)
        r = sum(weights)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if can_ship(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
