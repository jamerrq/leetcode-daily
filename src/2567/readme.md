# [2567. Minimum Score by Changing Two Elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an integer array `nums`.

- The **low** score of `nums` is the **minimum** absolute difference between any two integers.
- The **high** score of `nums` is the **maximum** absolute difference between any two integers.
- The **score** of `nums` is the sum of the **high** and **low** scores.

Return the **minimum score** after **changing two elements** of `nums`.

## Examples

### Example 1:

`Input: nums = [1,4,7,8,5]`

`Output: 3`

#### Explanation:

- Change `nums[0]` and `nums[1]` to be 6 so that `nums` becomes [6,6,7,8,5].
- The low score is the minimum absolute difference: |6 - 6| = 0.
- The high score is the maximum absolute difference: |8 - 5| = 3.
- The sum of high and low score is 3.

### Example 2:

`Input: nums = [1,4,3]`

`Output: 0`

#### Explanation:

- Change `nums[1]` and `nums[2]` to 1 so that `nums` becomes [1,1,1].
- The sum of maximum absolute difference and minimum absolute difference is 0.

## Constraints

- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## My Solution
[index.py](./index.py)

```python
from heapq import nsmallest, nlargest


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        a, b, c = nsmallest(n=3, iterable=nums)
        x, y, z = nlargest(n=3, iterable=nums)

        return min(x - c, y - b, z - a)
```

## Runtime
5 ms | Beats 97.13% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
31.36 MB | Beats 32.64%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-score-by-changing-two-elements/description)
