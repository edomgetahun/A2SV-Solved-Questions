class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(matrix[i][j])
        heapq.heapify(temp)
        for _ in range(k-1):
            heapq.heappop(temp)
        return heapq.heappop(temp)