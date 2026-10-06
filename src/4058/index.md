# [4058. Maximum Pulse Value After One Subarray Rotation](https://leetcode.com/problems/maximum-pulse-value-after-one-subarray-rotation/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an integer array `nums` of length `n`.

Define the pulse value of an integer array `arr` as the alternating sum starting at index 0: `pulse(arr) = arr[0] - arr[1] + arr[2] - arr[3] + ....`

You may perform at most one operation on `nums`:

- Choose two indices `l` and `r` such that `0 <= l < r < n`.
- Left-rotate the subarray `nums[l..r]` by exactly one position. For example, `[a, b, c, d]` becomes `[b, c, d, a]`.

Return the maximum pulse value that can be obtained after performing at most one such operation.

## Examples

### Example 1:

`Input: nums = [1,5,2]`

`Output: 6`

Explanation:

The original pulse value is 1 - 5 + 2 = -2.

Rotate the subarray nums[0..1] from [1, 5] to [5, 1].

The resulting array is [5, 1, 2] and its pulse value is 5 - 1 + 2 = 6, which is the maximum possible.

### Example 2:

`Input: nums = [6,4,3]`

`Output: 7`

Explanation:

The original pulse value is 6 - 4 + 3 = 5.

Rotate the subarray nums[1..2] from [4, 3] to [3, 4].

The resulting array is [6, 3, 4] and its pulse value is 6 - 3 + 4 = 7, which is the maximum possible.

### Example 3:

`Input: nums = [9,7]`

`Output: 2`

Explanation:

The original pulse value is 9 - 7 = 2, which is already maximum. Thus, no rotation is required.

## Constraints

- `1 <= n == nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def maxValue(self, nums: list[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)

        for i in range(n):
            P[i + 1] = P[i] + (-nums[i] if i % 2 else nums[i])

        maxEvenP = [0] * n
        maxOddP = [0] * n

        maxEvenP[0] = P[1]
        maxOddP[0] = P[0]

        for i in range(1, n):
            if i % 2:
                maxEvenP[i] = maxEvenP[i - 1]
                maxOddP[i] = max(maxOddP[i - 1], P[i + 1])
            else:
                maxEvenP[i] = max(maxEvenP[i - 1], P[i + 1])
                maxOddP[i] = maxOddP[i - 1]

        ans = 0
        for r in range(1, n):
            gain = maxEvenP[r - 1]
            if r % 2:
                gain = maxOddP[r - 1]
            cand = 2 * (gain - P[r + 1])
            ans = max(cand, ans)

        return P[-1] + ans
```

## Brief Explanation

One of the first problems solved for this project. I was heavily guided by this hint:

```
Let P[t] be the alternating sum of the first t elements, with P[0] = 0. The change in pulse value is 2 * (P[l + 1] - P[r + 1]) when l and r have the same parity, and 2 * (P[l] - P[r + 1]) otherwise.
```
And also this other one:

```
Scan r from left to right. Among indices l < r, maintain the maximum values of P[l] and P[l + 1] separately for each parity of l. Use these maxima to find the best gain in constant time per index, allowing a gain of zero for skipping the operation.
```

## Runtime
385 ms | Beats 28.80%

## Memory
35.29 MB | Beats 91.01% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximum-pulse-value-after-one-subarray-rotation/description)
