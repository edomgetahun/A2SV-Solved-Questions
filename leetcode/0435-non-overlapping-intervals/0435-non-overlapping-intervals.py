class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: x[1]) # sort by end points so we can track the one which intervals ends first this helps to maximize the remaining non overlaping intervals
        removed = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
        return removed

            