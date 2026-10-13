# [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/description)

**Level**: <span style="color:cyan">Easy</span>

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return *them in the form of an array*.

## Examples

### Example 1:

`Input: nums = [1,2,2,4]`

`Output: [2,3]`

### Example 2:

`Input: nums = [1,1]`

`Output: [1,2]`

## Constraints

- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        f = [0] * len(nums)
        ans = [0, 0]
        for num in nums:
            f[num - 1] += 1
            if f[num - 1] == 2:
                ans[0] = num

        for i in range(len(nums)):
            if not f[i]:
                ans[1] = i + 1
                break

        return ans
```

## Brief Explanation
We just simply iterate over the array checking for the first duplicate.
And a second time looking for the one that doesn't appear in `nums`.

## Runtime
15 ms | Beats 50.64% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
20.62 MB | Beats 95.93% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/set-mismatch/description)
