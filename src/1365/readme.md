# [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description)

**Level**: <span style="color:cyan">Easy</span>

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] < nums[i]`.

Return the answer in an array.

## Examples

### Example 1:

`Input: nums = [8,1,2,2,3]`

`Output: [4,0,1,1,3]`

#### Explanation:

- For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
- For nums[1]=1 does not exist any smaller number than it.
- For nums[2]=2 there exist one smaller number than it (1).
- For nums[3]=2 there exist one smaller number than it (1).
- For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

### Example 2:

`Input: nums = [6,5,4,8]`

`Output: [2,1,0,3]`

### Example 3:

`Input: nums = [7,7,7,7]`

`Output: [0,0,0,0]`

## Constraints

- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        z = list(zip(nums, list(range(n))))
        z.sort()

        count, same, prev = 0, 0, z[0][0]
        for i in range(1, n):
            num, idx = z[i]
            if num > prev:
                count += 1 + same
                same = 0
            if num == prev:
                same += 1

            ans[idx] = count
            prev = num

        return ans
```

## Brief Explanation

To achieve this optimally, we can sort the array, but saving each element along
with its index in order to know where to store each answer. Then we iterate the
numbers in increasing order, counting how many are below the current number, and
also storing if the current number is equal to the previous one, because these
positions share the same count, so the count is not updated here, only the range
of the current number counts.

As we did this in order, no element is skipped and we iterate once over the
list, so it's optimal. Also notice that we skipped the first element; this is
because it's the minimum of the list so it will always have a count of 0.

## Runtime
4 ms | Beats 71.03% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.31 MB | Beats 23.80% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description)
