# [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/)

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce `x` to exactly `0` if it is possible, otherwise, return `-1`.

**Level**: <span style="color:yellow">Medium</span>

## Examples

### Example 1:

`Input: nums = [1,1,4,2,3], x = 5`

`Output: 2`

#### Explanation:

The optimal solution is to remove the last two elements to reduce x to zero.

### Example 2:

`Input: nums = [5,6,7,8,9], x = 4`

`Output: -1`

### Example 3:

`Input: nums = [3,2,20,1,1,3], x = 10`

`Output: 5`

#### Explanation:

The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= x <= 10^9`

## My Solution

[index.py](./index.py)

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)
        mem = {0: -1}
        csi = 0
        ans = -1
        for i in range(n):
            csi += nums[i]
            mem[csi] = i
            index = mem.get(csi - (s - x))
            if index is not None:
                ans = max(ans, i - index)

        return n - ans if ans != -1 else ans
```

## Brief Explanation

As the hints suggests, solving this problem is the same as finding the maximum
subarray, this can be done by iterating over `nums` and in each position `look`
for a subarray ending at that position whose sum is equal to `S - x`, where S is
the total sum of the  `nums` array. Among all the possible solutions, the
longest sub array is chosen in order to left with the minimum

## Runtime

172 ms | Beats 11.64%

## Memory

43.84 MB | Beats 5.61%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero)