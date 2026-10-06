from bisect import bisect_right

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        intervals.sort()
        starts = [intv[0] for intv in intervals]

        for i, interval in enumerate(intervals):
            index = bisect_right(starts, interval[1], lo=i+1)
            print(index)

        return ans

intervals = [[1,2],[2,3],[3,4]]
sol = Solution()
print(sol.countIntersectingIntervals(intervals))