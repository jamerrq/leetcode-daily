# [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description)

**Level**: <span style="color:yellow">Medium</span>

Given an array of integers `arr`, return *the number of subarrays with an **odd** sum*.

Since the answer can be very large, return it modulo `10^9 + 7`.

## Examples

### Example 1:

`Input: arr = [1,3,5]`

`Output: 4`

#### Explanation:

- All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
- All sub-arrays sum are [1,4,9,3,8,5].
- Odd sums are [1,9,3,5] so the answer is 4.

### Example 2:

`Input: arr = [2,4,6]`

`Output: 0`

#### Explanation:

- All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
- All sub-arrays sum are [2,6,12,4,10,6].
- All sub-arrays have even sum and the answer is 0.

### Example 3:

`Input: arr = [1,2,3,4,5,6,7]`

`Output: 16`

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 100`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        partial_sum = 0
        even_partial_sums = 1  # 0 as starting sum is even
        odd_partial_sums = 0

        for num in arr:
            partial_sum += num

            if partial_sum % 2 == 0:
                ans = (ans + odd_partial_sums) % MOD
                even_partial_sums += 1
            else:
                ans = (ans + even_partial_sums) % MOD
                odd_partial_sums += 1

        return ans
```

## Runtime
74 ms | Beats 47.22%

## Memory
24.51 MB | Beats 38.21%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description)
