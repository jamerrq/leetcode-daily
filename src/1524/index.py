class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        MOD = 10**9 + 7
        partial_sum = 0
        even_partial_sums = 1  # 0 as starting sum is even
        odd_partial_sums = 0

        for num in arr:
            partial_sum += num

            if partial_sum % 2 == 0:
                ans = (ans + odd_partial_sums) % MOD
                even_partial_sums += 1
            else:
                ans = (ans + even_partial_sums) % MOD
                odd_partial_sums += 1

        return ans
