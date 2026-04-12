class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        cols = set()
        left_d = set()
        right_d = set()
        q = []
        def helper(r):
            if r == n:
                self.cnt += 1
            for c in range(n):
                if c not in cols and r-c not in left_d and r+c not in right_d:
                    cols.add(c)
                    left_d.add(r-c)
                    right_d.add(r+c)
                    q.append((r,c))
                    
                    helper(r+1)
                    cols.remove(c)
                    left_d.remove(r-c)
                    right_d.remove(r+c)
                    q.pop()
        helper(0)
        return self.cnt