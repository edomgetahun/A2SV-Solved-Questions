class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -(heapq.heappop(stones))
            sec = -(heapq.heappop(stones))
            if first != sec:
                heapq.heappush(stones, -(first-sec))

        if stones:
            return -(stones[0])
        return 0 