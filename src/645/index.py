class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        f = [0] * len(nums)
        ans = [0, 0]
        for num in nums:
            f[num - 1] += 1
            if f[num - 1] == 2:
                ans[0] = num

        for i in range(len(nums)):
            if not f[i]:
                ans[1] = i + 1
                break

        return ans