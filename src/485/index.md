# [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/description)

**Level**: <span style="color:cyan">Easy</span>

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array*.

## Examples

### Example 1:

`Input: nums = [1,1,0,1,1,1]`

`Output: 3`

#### Explanation:

The first two digits or the last three digits are consecutive `1`s. The maximum number of consecutive `1`s is 3.

### Example 2:

`Input: nums = [1,0,1,1,0,1]`

`Output: 2`

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr, ans = 0, 0
        for num in nums:
            if num:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0

        return ans
```

## Brief Explanation
We just simply check at each `1` if the current `1`s streak is greater than the current answer, and return at the end the largest one.

## Runtime
23 ms | Beats 22.16%

## Memory
21.92 MB | Beats 18.68%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/max-consecutive-ones/description)
