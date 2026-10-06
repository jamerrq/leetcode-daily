# [4056. Number of Intersecting Interval Pairs I](https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/description/)

**Level**: <span style="color:cyan">Easy</span>

You are given a 2D integer array `intervals` of `n` elements, where $intervals[i] = [start_i, end_i]$ represents the closed interval from $start_i$ to $end_i$.

Return the number of pairs of indices `(i, j)` such that `0 <= i < j < n` and `intervals[i]` and `intervals[j]` intersect.

Two intervals intersect if they have at least one point in common, including when they only share an endpoint.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        ans = 0
        for i in range(n):
            ii = intervals[i]
            for j in range(i + 1, n):
                ij = intervals[j]
                xl = max(ii[0], ij[0])
                yl = min(ii[1], ij[1])
                if xl <= yl:
                    ans += 1

        return ans
```

## Brief Explanation

As the description says, two intervals $[x_i,y_i]$ and $[x_j,y_j]$ intersect if they share any point in common. The common part is defined as $[\max(x_i, x_j), \min(y_i,y_j)]$ if this interval is valid, i.e. $\max(x_i, x_j) \leq \min(y_i,y_j)$. With this definition, we can iterate over every pair of intervals and count the ones whose common part is valid.

## Runtime

87 ms | Beats 22.01%

## Memory

19.3 MB | Beats 33.50%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/)