class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        cum_sum = [0] * (n + 1)
        r_cum_sum = [0] * (n + 1)
        #
        m, r_m = {}, {}
        #
        for i in range(n):
            cum_sum[i+1] = cum_sum[i] + arr[i]
            m[cum_sum[i + 1]] = i
            r_cum_sum[-i-2] = r_cum_sum[-i-1] + arr[-i-1]
            r_m[r_cum_sum[-i-2]] = n - i - 1
        #
        prefix = [float('inf')] * n
        suffix = [float('inf')] * n
        for i in range(n):
            # first case, arr[i] == target
            if arr[i] == target:
                prefix[i] = 1
            if arr[-i-1] == target:
                suffix[-i-1] = 1
            # second case, cum_sum[i + 1] == target
            # prefix[i] would be min between prefix[i - 1] and i + 1
            if cum_sum[i + 1] == target:
                prefix[i] = min(prefix[i - 1], i + 1)
            if r_cum_sum[-i-2] == target:
                if n == 1:
                    suffix[-i-1] = i + 1
                    continue
                suffix[-i-1] = min(suffix[-i-2], i + 1)
            # third case, cum_sum[i] - target exists in m
            left = cum_sum[i + 1] - target
            index = m.get(left, None)
            if index is not None:
                prefix[i] = min(i - index, prefix[i - 1])
            r_left = r_cum_sum[-i-2] - target
            r_index = r_m.get(r_left, 0)
            if r_index:
                suffix[-i-1] = min(r_index - n + i + 1, suffix[-i-1])

            prefix[i] = min(prefix[i], prefix[i - 1])
            suffix[-i-1] = min(suffix[-i-1], suffix[-i])
        #
        ans = float('inf')
        for i in range(1, n - 1):
            pi = prefix[i]
            si = suffix[i + 1]
            if pi + si != float('inf'):
                ans = min(ans, pi + si)

        if ans > n:
            return -1
        return ans
