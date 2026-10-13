# [3871. Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an integer `n`.

Return the total number of commas used when writing all integers from `[1, n]` (inclusive) in standard number formatting.

In standard formatting:

- A comma is inserted after every three digits from the right.
- Numbers with fewer than 4 digits contain no commas.

## Examples

### Example 1:

`Input: n = 1002`

`Output: 3`

#### Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

### Example 2:

`Input: n = 998`

`Output: 0`

#### Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

## Constraints

- `1 <= n <= 10^15`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def countCommas(self, n: int) -> int:
        mm = 0
        if n == 1e15:
            mm = 5

        zz = max(0, min(1e15 - 1, n) - 1e12 + 1)
        yy = max(0, min(1e12 - 1, n) - 1e9 + 1)
        xx = max(0, min(1e9 - 1, n) - 1e6 + 1)
        vv = max(0, min(1e6 - 1, n) - 1e3 + 1)

        return int(zz * 4 + yy * 3 + xx * 2 + vv + mm)
```

### Another approach (simpler)

```python
class Solution:
    def countCommas(self, n: int) -> int:
        p, res = 1000, 0
        while p <= n:
            res += n - p + 1
            p *= 1000
        return res
```

## Brief Explanation

We can divide the nums from 1000 to n into groups, each number goes to the group with the numbers that have the same amount of commas, so from 1,000 to 999,999 goes to a group, from 1,000,000 to 999,999,999 goes to another group and so on, since we know the limit for the input, we can make this count in O(1).

### Simpler approach
We start with the base case p = 1000, while p is at most n, let's add the numbers between them, and then, p goes to the beginning of the next group (same definition as above).

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.24 MB | Beats 50.12% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/count-commas-in-range-ii/description)
