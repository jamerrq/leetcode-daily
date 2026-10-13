# [4066. Maximum Equal Adjacent Pairs After at Most One Replacement](https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a 1-indexed integer array `nums`.

You can choose two distinct values `x` and `y` and perform the following operation at most once:

- Replace every occurrence of `x` in `nums` with `y`.

Return the maximum possible number of pairs of adjacent elements that are equal after performing the operation.

## Examples

### Example 1:

`Input: nums = [1,2,3,2]`

`Output: 2`

#### Explanation:

- One optimal solution is to choose x = 3 and y = 2.
- The resulting array is [1, 2, 2, 2].
- There are 2 pairs of adjacent elements that are equal: (nums[2], nums[3]) and (nums[3], nums[4]).
- Therefore, the answer is 2.

### Example 2:

`Input: nums = [1,2,1,2,1]`

`Output: 4`

#### Explanation:

- One optimal solution is to choose x = 1 and y = 2.
- The resulting array is [2, 2, 2, 2, 2].
- There are 4 pairs of adjacent elements that are equal: (nums[1], nums[2]), (nums[2], nums[3]), (nums[3], nums[4]), and (nums[4], nums[5]).
- Therefore, the answer is 4.

### Example 3:

`Input: nums = [1,1,1]`

`Output: 2`

#### Explanation:

- One optimal solution is to perform no operation.
- Thus, the resulting array is [1, 1, 1].
- There are 2 pairs of adjacent elements that are equal: (nums[1], nums[2]) and (nums[2], nums[3]).
- Therefore, the answer is 2.

## Constraints

- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## My Solution
[index.py](./index.py)

```python
from itertools import pairwise

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        pairs = {}
        pairs_count = 0
        most_frequent_pair_count = 0
        for prev, num in pairwise(nums):
            pair = (prev, num)
            if num < prev:
                pair = (num, prev)

            if num != prev:
                pairs[pair] = pairs.get(pair, 0) + 1
                most_frequent_pair_count = max(
                    most_frequent_pair_count, pairs[pair]
                )
            else:
                pairs_count += 1

        return most_frequent_pair_count + pairs_count
```

## Brief Explanation

We can divide the array nums into pairs nums[i] and nums[i + 1] for each i below n - 1. Then we iterate counting the amount of times each pair appears but having in mind that the order doesn't matter for a pair to be unique, i.e. (2, 3) must count as the same as (3, 2). If we find a pair of equal elements, it will go to the answer anyway so we add it to the final answer.
At the end, we add the frequency of the most frequent pair with distinct elements.

## Runtime
340 ms | Beats 90.05% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
42.02 MB | Beats 90.37% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement/description)
