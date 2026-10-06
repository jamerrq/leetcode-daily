class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq = [0] * 101
        max_freq = 0
        unique = set()
        for num in nums:
            freq[num] = freq[num] + 1
            max_freq = max(max_freq, freq[num])
            unique.add(num)
        #
        ans = []
        unique_list = list(unique)
        unique_list.sort()
        for f in range(1, max_freq + 1): # max (n)
            for num in unique_list: # max n
                if freq[num] >= f:
                    ans.append(num)

        return ans
