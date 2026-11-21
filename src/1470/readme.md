# [1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/description)

**Level**: <span style="color:cyan">Easy</span>

Given the array `nums` consisting of `2n` elements in the form `[x_1,x_2,...,x_n,y_1,y_2,...,y_n]`.

*Return the array in the form* `[x_1,y_1,x_2,y_2,...,x_n,y_n]`.

## Examples

### Example 1:

`Input: nums = [2,5,1,3,4,7], n = 3`

`Output: [2,3,5,4,1,7]`

#### Explanation:

Since `x_1=2`, `x_2=5`, `x_3=1`, `y_1=3`, `y_2=4`, `y_3=7`, then the answer is `[2,3,5,4,1,7]`.

### Example 2:

`Input: nums = [1,2,3,4,4,3,2,1], n = 4`

`Output: [1,4,2,3,3,2,4,1]`

### Example 3:

`Input: nums = [1,1,2,2], n = 2`

`Output: [1,2,1,2]`

## Constraints

- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_nums = [0] * (2 * n)
        for i in range(n):
            xi = nums[i]
            yi = nums[n + i]
            new_nums[2 * i] = xi
            new_nums[2 * i + 1] = yi

        return new_nums
```

## Brief Explanation

We can spot that the number indexes in the new array follow this pattern:
$shuffledNumsIndexes = [i, n + i, i + 1, n + i + 1, i + 2 ...] \ for\ i \in [1, 2, \dots, n]$
that is, $i + n // i$ for odd indexes, and $n + i + n // i$ for even indexes,
with $//$ known as integer division. So we can iterate over the given array
assigning each element to its new position.

## Runtime
69 ms | Beats 22.97%

## Memory
19.48 MB | Beats 17.75% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/shuffle-the-array/description)
