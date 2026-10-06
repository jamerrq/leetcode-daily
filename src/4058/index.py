class Solution:
    def maxValue(self, nums: list[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)

        for i in range(n):
            P[i + 1] = P[i] + nums[i] * (-1) ** i

        maxEvenP = [0] * n
        maxOddP = [0] * n

        maxEvenP[0] = P[1]
        maxOddP[0] = P[0]

        for i in range(1, n):
            if i % 2:
                maxEvenP[i] = maxEvenP[i - 1]
                maxOddP[i] = max(maxOddP[i - 1], P[i + 1])
            else:
                maxEvenP[i] = max(maxEvenP[i - 1], P[i + 1])
                maxOddP[i] = maxOddP[i - 1]

        ans = 0
        for r in range(1, n):
            gain = maxEvenP[r - 1]
            if r % 2:
                gain = maxOddP[r - 1]
            cand = 2 * (gain - P[r + 1])
            ans = max(cand, ans)

        return P[-1] + ans