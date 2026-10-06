# [4057. Number of Intersecting Interval Pairs II](https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a 2D integer array `intervals` of `n` elements, where $intervals[i] = [start_i, end_i]$ represents the closed interval from $start_i$ to $end_i$.

Return the number of pairs of indices `(i, j)` such that `0 <= i < j < n` and `intervals[i]` and `intervals[j]` intersect.

Two intervals intersect if they have at least one point in common, including when they only share an endpoint.

## Examples

### Example 1:

`Input: intervals = [[1,2],[2,3],[3,4]]`

`Output: 2`

Explanation: There are 2 intersecting interval pairs:

- Intervals `[1, 2]` and `[2, 3]` intersect at the point `2`.
- Intervals `[2, 3]` and `[3, 4]` intersect at the point `3`.

### Example 2:

`Input: intervals = [[1,5],[2,4],[3,6]]`

`Output: 3`

Explanation:

There are 3 intersecting interval pairs:

- The intersection of `[1, 5]` and `[2, 4]` is `[2, 4]`.
- The intersection of `[1, 5]` and `[3, 6]` is `[3, 5]`.
- The intersection of `[2, 4]` and `[3, 6]` is `[3, 4]`.

### Example 3:

`Input: intervals = [[1,2],[3,4],[5,6]]`

`Output: 0`

Explanation:

There are no intersecting interval pairs. Hence, the answer is 0.

## Constraints

- `2 <= n == intervals.length <= 10⁵`
- $intervals[i] = [start_i, end_i]$
- $0 \le start_i \le end_i \le 10^9$

## My Solution
[index.py](./index.py)

```python
from bisect import bisect_right

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        intervals.sort()
        starts = [intv[0] for intv in intervals]

        for i, interval in enumerate(intervals):
            index = bisect_right(starts, interval[1], lo=i+1)
            ans += index - i - 1

        return ans
```

## Brief Explanation

If we sort the intervals by their start, then for each interval we only need to count how many of the following ones intersect it. Those are exactly the ones that start before (or at) its closing point, so we find the last one that does. Since the starts are sorted, this can be done with binary search.

## Runtime
250 ms | Beats 35.28%

## Memory
59.18 MB | Beats 35.97%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/description)
