# [4065. Rearrange Array by Removing Distinct Values](https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/description)

**Level**: <span style="color:cyan">Easy</span>

You are given an integer array `nums`.

You start with an empty array `ans`. Repeat the following operation until `nums` is empty:

- Identify all distinct values currently present in `nums`.
- Remove one occurrence of every distinct value currently in `nums`, and append those values to `ans` in ascending order.

Return the array `ans`.

## Examples

### Example 1:

`Input: nums = [3,1,3,2,1,3]`

`Output: [1,2,3,1,3,3]`

Explanation:

| Operation | Appended to `ans` | `nums` after | `ans` after |
| ---: | --- | --- | --- |
| 1 | 1, 2, 3 | `[3, 1, 3]` | `[1, 2, 3]` |
| 2 | 1, 3 | `[3]` | `[1, 2, 3, 1, 3]` |
| 3 | 3 | `[]` | `[1, 2, 3, 1, 3, 3]` |

`nums` is now empty, so the answer is `[1, 2, 3, 1, 3, 3]`.

### Example 2:

`Input: nums = [7,7,4,4,4]`

`Output: [4,7,4,7,4]`

Explanation:

| Operation | Appended to `ans` | `nums` after | `ans` after |
| ---: | --- | --- | --- |
| 1 | 4, 7 | `[7, 4, 4]` | `[4, 7]` |
| 2 | 4, 7 | `[4]` | `[4, 7, 4, 7]` |
| 3 | 4 | `[]` | `[4, 7, 4, 7, 4]` |

`nums` is now empty, so the answer is `[4, 7, 4, 7, 4]`.

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## My Solution
[index.py](./index.py)

```python
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
```

## Brief Explanation

We can notice a pattern: the most frequent number appears in all the groups, and in general, a number that appears `k` times is in the first `k` groups.

So, to solve the problem, we first store the frequency of each number, and at the same time identify the set of unique numbers and the maximum frequency (in the worst case, when all the numbers are the same, this would be `n`). With this, we iterate over the frequencies (from 1 to the max), and for each one, we iterate over the sorted unique numbers. As the frequency grows, the number of unique numbers that appear shrinks.

## Runtime
7 ms | Beats 70.35% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.26 MB | Beats 78.29% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/description)
