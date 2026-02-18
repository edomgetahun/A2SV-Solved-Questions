class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n , m = len(img), len(img[0])
        res = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                total , count = 0, 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or i == n or j < 0 or j == m:
                            continue
                        total += img[i][j]
                        count += 1
                average = total//count
                res[r][c] = average
        return res
