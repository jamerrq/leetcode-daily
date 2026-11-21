# [3364. Minimum Positive Sum Subarray ](https://leetcode.com/problems/minimum-positive-sum-subarray/description)

**Level**: <span style="color:cyan">Easy</span>

You are given an integer array `nums` and **two** integers `l` and `r`. Your task is to find the **minimum** sum of a **subarray** whose size is between `l` and `r` (inclusive) and whose sum is greater than 0.

Return the **minimum** sum of such a subarray. If no such subarray exists, return -1.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Examples

### Example 1:

`Input: nums = [3, -2, 1, 4], l = 2, r = 3`

`Output: 1`

#### Explanation:

The subarrays of length between `l = 2` and `r = 3` where the sum is greater than 0 are:

- `[3, -2]` with a sum of 1
- `[1, 4]` with a sum of 5
- `[3, -2, 1]` with a sum of 2
- `[-2, 1, 4]` with a sum of 3

Out of these, the subarray `[3, -2]` has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

### Example 2:

`Input: nums = [-2, 2, -3, 1], l = 2, r = 3`

`Output: -1`

#### Explanation:

There is no subarray of length between `l` and `r` that has a sum greater than 0. So, the answer is -1.

### Example 3:

`Input: nums = [1, 2, 3, 4], l = 2, r = 4`

`Output: 3`

#### Explanation:

The subarray `[1, 2]` has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

## Constraints

- `1 <= nums.length <= 100`
- `1 <= l <= r <= nums.length`
- `-1000 <= nums[i] <= 1000`

## My Solution
[main.c](./main.c)

```C
int minimumSumSubarray(int *nums, int numsSize, int l, int r) {
  int ans = -1;
  for (int i = 0; i < numsSize; ++i) {
    int stop = numsSize < i + r ? numsSize : i + r;
    for (int j = i + l - 1; j < stop; ++j) {
      int curr_sum = 0;
      for (int index = i; index < j + 1; ++index)
        curr_sum += nums[index];
      if (curr_sum > 0) {
        ans = ans == -1 && curr_sum > 0 ? curr_sum : ans;
        ans = ans < curr_sum ? ans : curr_sum;
      }
    }
  }
  return ans;
}
```

## Runtime
5 ms | Beats 15.12%

## Memory
9.67 MB | Beats 77.09% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-positive-sum-subarray/description)
