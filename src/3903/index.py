class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxCum = [0] * n
        minCum = [0] * n
        maxCum[0] = nums[0]
        minCum[-1] = nums[-1]
        for i in range(n - 1):
            maxCum[i+1] = max(nums[i+1], maxCum[i])
            minCum[-i-2] = min(nums[-i-2], minCum[-i-1])
        ans = -1
        for i in range(n):
            diff = maxCum[i] - minCum[i]
            if diff <= k:
                return i

        return ans