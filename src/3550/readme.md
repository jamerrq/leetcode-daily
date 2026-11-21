# [3550. Smallest Index With Digit Sum Equal to Index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/)

You are given an integer array `nums`.

Return the smallest index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

**Level**: <span style="color:cyan">Easy</span>

## Examples

### Example 1:

`Input: nums = [1,3,2]`

`Output: 2`

#### Explanation:

- For `nums[2] = 2`, the sum of digits is 2, which is equal to index `i = 2`. Thus, the output is 2.

### Example 2:

`Input: nums = [1,10,11]`

`Output: 1`

#### Explanation:

- For `nums[1] = 10`, the sum of digits is `1 + 0 = 1`, which is equal to index `i = 1`.
- For `nums[2] = 11`, the sum of digits is `1 + 1 = 2`, which is equal to index `i = 2`.
- Since index 1 is the smallest, the output is 1.

### Example 3:

`Input: nums = [1,2,3]`

`Output: -1`

#### Explanation:

- Since no index satisfies the condition, the output is -1.

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## My Solution

[index.py](./index.py)

```python
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digits_sum(num):
            if num < 10:
                return num
            return num % 10 + digits_sum(num // 10)

        n = len(nums)
        for i in range(n):
            if i == digits_sum(nums[i]):
                return i

        return -1
```

### C Implementation

[main.c](./main.c)
```c
static int digitsSum(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (digitsSum(nums[i]) == i) {
            return i;
        }
    }
    return -1;
}
```

## Brief Explanation

This is probably the easiest problem I've ever found on the platform. Such as
that, I decided to update this upstream repo before daily problem reset (00:00h
at UTC) (I wasn't doing this in case any of the 0 repo viewers get spoiled).

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.52 MB Beats | 5.72%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index)