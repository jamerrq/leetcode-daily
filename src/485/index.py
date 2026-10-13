class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr, ans = 0, 0
        for num in nums:
            if num:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0

        return ans