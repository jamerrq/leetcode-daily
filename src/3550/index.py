class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digits_sum(num):
            if num < 10:
                return num
            return num % 10 + digits_sum(num // 10)

        n = len(nums)
        for i in range(n):
            if i == digits_sum(nums[i]):
                return i

        return -1