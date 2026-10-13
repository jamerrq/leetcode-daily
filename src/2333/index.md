# [2333. Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/description)

**Level**: <span style="color:yellow">Medium</span>

You are given two positive **0-indexed** integer arrays `nums1` and `nums2`, both of length `n`.

The **sum of squared difference** of arrays `nums1` and `nums2` is defined as the **sum** of `(nums1[i] - nums2[i])^2` for each `0 <= i < n`.

You are also given two positive integers `k1` and `k2`. You can modify any of the elements of `nums1` by `+1` or `-1` at most `k1` times. Similarly, you can modify any of the elements of `nums2` by `+1` or `-1` at most `k2` times.

Return *the minimum **sum of squared difference** after modifying array `nums1` at most `k1` times and modifying array `nums2` at most `k2` times*.

**Note**: You are allowed to modify the array elements to become **negative** integers.

## Examples

### Example 1:

`Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0`

`Output: 579`

#### Explanation:

- The elements in `nums1` and `nums2` cannot be modified because `k1 = 0` and `k2 = 0`.
- The sum of squared difference will be: `(1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579`.

### Example 2:

`Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1`

`Output: 43`

#### Explanation:

- One way to obtain the minimum sum of squared difference is:
  - Increase `nums1[0]` once.
  - Increase `nums2[2]` once.
- The minimum of the sum of squared difference will be:
- `(2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43`.
- Note that there are other ways to obtain the minimum of the sum of squared difference, but there is no way to obtain a sum smaller than 43.

## Constraints

- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^5`
- `0 <= k1, k2 <= 10^9`

## My Solution
[index.py](./index.py)

```python
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
```

## Explanation
The first thing to notice is that it is the same thing doing the operation in one array or another, since we want to reduce the distance between paired elements. So the budget is always the same: `k = k1 + k2`. The second thing to notice is that the best thing we can do is to reduce the greatest distance. Why? Suppose we have the distances array:

$d_1,d_2,\dots,d_n$ where $d_i = |nums1_i - nums2_i|$

This would have a squared sum of

$d_1^2 + d_2^2+\dots+d_n^2$

If we decrease $d_i$ by one unit, its contribution to the sum becomes

$(d_i-1)^2 = d_i^2 - 2d_i + 1$

Which means that the overall sum gets decreased by $-2d_i+1$ and for this to be optimal $d_i$ has to be the greatest in the array.

With that in mind, we can sort and store the differences in a stack along with their frequencies, so that in each step we calculate the cost to level down to the next greatest difference. If `k` is enough, we do this and advance; if it is not enough or there is no next difference, we distribute `k` among these greatest elements and manually add the rest.

## Runtime
71 ms | Beats 99.41% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
45.76 MB | Beats 5.07%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-sum-of-squared-difference/description)
