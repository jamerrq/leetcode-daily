class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_nums = [0] * (2 * n)
        for i in range(n):
            xi = nums[i]
            yi = nums[n + i]
            new_nums[2 * i] = xi
            new_nums[2 * i + 1] = yi

        return new_nums