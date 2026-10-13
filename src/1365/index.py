class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        z = list(zip(nums, list(range(n))))
        z.sort()

        count, same, prev = 0, 0, z[0][0]
        for i in range(1, n):
            num, idx = z[i]
            if num > prev:
                count += 1 + same
                same = 0
            if num == prev:
                same += 1

            ans[idx] = count
            prev = num

        return ans