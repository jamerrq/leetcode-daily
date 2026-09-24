# [3550. Smallest Index With Digit Sum Equal to Index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/)

You are given an integer array `nums`.

Return the smallest index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

**Level**: <span style="color:cyan">Easy</span>

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

## Brief Explanation

This is probably the easiest problem I've ever found on the platform.
Such as that, I decided to update this upstream repo before daily problem reset (00:00h at UTC) (I wasn't doing this in case any of the 0 repo viewers get spoiled).

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.52 MB Beats | 5.72%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index)