from heapq import nsmallest, nlargest


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        a, b, c = nsmallest(n=3, iterable=nums)
        x, y, z = nlargest(n=3, iterable=nums)

        return min(x - c, y - b, z - a)
