# [3524. Find X Value of Array I](https://leetcode.com/problems/find-x-value-of-array-i/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an array of **positive** integers `nums`, and a positive integer `k`.

You are allowed to perform an operation once on `nums`, where in each operation you can remove any non-overlapping prefix and suffix from `nums` such that `nums` remains non-empty.

You need to find the x-value of `nums`, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of `x` when divided by `k`.

Return an array `result` of size `k` where `result[x]` is the x-value of `nums` for `0 <= x <= k - 1`.

A **prefix** of an array is a subarray[^1] that starts from the beginning of the array and extends to any point within it.

A **suffix** of an array is a subarray[^1] that starts at any point within the array and extends to the end of the array.

**Note** that the prefix and suffix to be chosen for the operation can be **empty**.

---

[^1]: A subarray is a contiguous sequence of elements within an array.

## Hints

### Hint 1
Use dynamic programming.

### Hint 2
Define `dp[i][r]` as the count of subarrays ending at index `i` whose product modulo `k` equals `r`.

### Hint 3
Compute `dp[i][r]` for each index `i` in `nums` and sum over all indices to get the final counts for each remainder.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        P = [0] * k
        ans = [x for x in P]
        #
        for i in range(n):
            T = [0] * k
            if nums[i] % k == 0:
                T[0] = i + 1
                ans[0] += i + 1
            else:
                for ki in range(k):
                    if not P[ki]:
                        continue
                    remainder = (ki * nums[i]) % k
                    T[remainder] += P[ki]
                    ans[remainder] += P[ki]
                T[nums[i] % k] += 1
                ans[nums[i] % k] += 1
            P = [x for x in T]

        return ans
```

## Brief Explanation
After reading the hints and some manual work, I got to the point where I'm able to define the number of intervals that contribute to each integer from `0` to `k` in base to the previous definition.

## Runtime

279 ms | Beats 90.41 ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

34.08 MB | Beats 84.93% ![clapping_hands](../../lib/clapping_hands.svg)


## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/find-x-value-of-array-i)