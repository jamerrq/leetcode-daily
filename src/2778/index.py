class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        ans, n = nums[0] ** 2, len(nums)
        for i in range(1, n):
            if n % (i + 1) == 0:
                ans += nums[i] ** 2

        return ans