# [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/?envType=daily-question&envId=2026-09-17)

**Level**: <span style="color:yellow">Medium</span>

You are given an array of integers `arr` and an integer `target`.

You have to find two non-overlapping sub-arrays of `arr` each with a sum equal `target`. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is **minimum**.

Return the minimum sum of the lengths of the two required sub-arrays, or return `-1` if you cannot find such two sub-arrays.

## My Solution

[index.py](./index.py)

```python
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
        #
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
```

## Explanation
This problem almost fried my lil brain.

As the leetcode hints suggests, one way to solve this problem is by creating
two arrays `prefix` and `suffix` such that they store the information about the current position and the possibility to create a solution at and index `i`.
So, let's define:

- `prefix[i]` would be the shortest sub-array we can choose before `i` (inclusive) that sums `target`
- `suffix[i]` would be the shortest sub array we can choose from `i` to end that sums `target`

Notice how some of this positions are not defined since there is no possible solution, in that case, the value is defined as infinite for practical purposes.

The answer will be iterating over the valid positions and choose the minimum one over `prefix[i] + suffix[i + 1]`, or `-1` if no valid solutions.

## Runtime

852 ms | Beats 5.02%

## Memory

57.73 MB | Beats 6.70%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/?envType=daily-question&envId=2026-09-17)