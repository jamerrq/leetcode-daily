# [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description)

**Level**: <span style="color:cyan">Easy</span>

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

## Examples

### Example 1:

`Input: nums = [4,3,2,7,8,2,3,1]`

`Output: [5,6]`

### Example 2:

`Input: nums = [1,1]`

`Output: [2]`

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        n, curr, index, ans = len(nums), 1, 0, []
        while curr <= n:
            if index >= n:
                ans.append(curr)
                curr += 1
                continue
            num = nums[index]
            if num > curr:
                ans.append(curr)
                curr += 1
            elif num == curr:
                curr += 1
                index += 1
            else:
                index += 1

        return ans
```

## Brief Explanation
We can check every number from `1` to `n` after sorting the `nums` array, tracking with an `index` whether the number is in the array or not. When we find the current number, we increase the `index` and the current number and advance; otherwise, it is because either the number at the current `index` is greater, in which case it means the current number we are looking for got skipped, so we have to add it to the final answer, or it is below, which means there were some duplicates in the array and we are below the target, so we advance. If we are out of the array limits, we just simply add everything missing from here to the end.

## Runtime
67 ms | Beats 5.60%

## Memory
30.75 MB | Beats 66.13% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description)
