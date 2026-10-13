from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        diff_with_freq = [(0, 0)] + sorted(Counter(diff).items())

        k = k1 + k2
        ans = 0
        while diff_with_freq:

            curr_diff, curr_freq = diff_with_freq.pop()

            if (not curr_diff) or (not curr_freq):
                break

            next_diff, next_freq = diff_with_freq[-1]
            to_match = (curr_diff - next_diff) * curr_freq

            if to_match <= k:
                k -= to_match
                new_freq = next_freq + curr_freq
                diff_with_freq[-1] = (next_diff, new_freq)

            else:
                to_reduce = min(k // curr_freq, curr_diff)
                curr_diff -= to_reduce
                k -= to_reduce * curr_freq
                # slice here between those who stay at
                # curr_diff - to_reduce (A) and those who
                # get down to curr_diff - to_reduce - 1 (B)
                A = curr_freq - k
                B = curr_freq - A
                # group A adds curr_diff * A
                ans += curr_diff ** 2 * A
                # group B is similar
                ans += (curr_diff - 1) ** 2 * B
                # nothing remains in k so elements from here to the end
                # can be added
                ans += sum((x[0] ** 2) * x[1] for x in diff_with_freq)
                break

        return ans