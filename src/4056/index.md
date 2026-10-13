# [4056. Number of Intersecting Interval Pairs I](https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/description/)

**Level**: <span style="color:cyan">Easy</span>

You are given a 2D integer array `intervals` of `n` elements, where $intervals[i] = [start_i, end_i]$ represents the closed interval from $start_i$ to $end_i$.

Return the number of pairs of indices `(i, j)` such that `0 <= i < j < n` and `intervals[i]` and `intervals[j]` intersect.

Two intervals intersect if they have at least one point in common, including when they only share an endpoint.

## Examples

### Example 1:

`Input: intervals = [[1,2],[2,3],[3,4]]`

`Output: 2`

#### Explanation:

There are 2 intersecting interval pairs:

- Intervals `[1, 2]` and `[2, 3]` intersect at the point 2.
- Intervals `[2, 3]` and `[3, 4]` intersect at the point 3.

### Example 2:

`Input: intervals = [[1,5],[2,4],[3,6]]`

`Output: 3`

#### Explanation:

There are 3 intersecting interval pairs:

- The intersection of `[1, 5]` and `[2, 4]` is `[2, 4]`.
- The intersection of `[1, 5]` and `[3, 6]` is `[3, 5]`.
- The intersection of `[2, 4]` and `[3, 6]` is `[3, 4]`.

### Example 3:

`Input: intervals = [[1,2],[3,4],[5,6]]`

`Output: 0`

#### Explanation:

There are no intersecting interval pairs. Hence, the answer is 0.

## Constraints

- `2 <= n == intervals.length <= 100`
- `intervals[i] = [start_i, end_i]`
- `0 <= start_i <= end_i <= 100`

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