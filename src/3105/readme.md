# [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description)

**Level**: <span style="color:cyan">Easy</span>

You are given an array of integers `nums`. Return *the length of the **longest** subarray of* `nums`* which is either **strictly increasing** or **strictly decreasing***.

## Examples

### Example 1:

`Input: nums = [1,4,3,3,2]`

`Output: 2`

#### Explanation:

The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`.

The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`.

Hence, we return `2`.

### Example 2:

`Input: nums = [3,3,3,3]`

`Output: 1`

#### Explanation:

The strictly increasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

Hence, we return `1`.

### Example 3:

`Input: nums = [3,2,1]`

`Output: 3`

#### Explanation:

The strictly increasing subarrays of `nums` are `[3]`, `[2]`, and `[1]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`.

Hence, we return `3`.

## Constraints

- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 50`

## My Solution
[main.c](./main.c)

```C
int longestMonotonicSubarray(int* nums, int numsSize){
    int longDec = 1, longInc = 1, currDec = 1, currInc = 1;
    int prev = nums[0];
    for (int i = 1; i < numsSize; ++i){
        if (nums[i] > prev) {
            currInc++;
            currDec = 1;
            if (currInc > longInc) longInc = currInc;
        } else if (nums[i] < prev) {
            currDec++;
            currInc = 1;
            if (currDec > longDec) longDec = currDec;
        } else {
            currInc = 1;
            currDec = 1;
        }
        prev = nums[i];
    }
    return longInc > longDec ? longInc : longDec;
}
```

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
9.53 MB | Beats 24.90%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description)
