class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            ii = intervals[i]
            for j in range(i + 1, n):
                ij = intervals[j]
                xl = max(ii[0], ij[0])
                yl = min(ii[1], ij[1])
                if xl <= yl:
                    ans += 1

        return ans