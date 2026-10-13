# [1963. Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a **0-indexed** string `s` of **even** length `n`. The string consists of **exactly** `n / 2` opening brackets `'['` and `n / 2` closing brackets `']'`.

A string is called **balanced** if and only if:

- It is the empty string, or
- It can be written as `AB`, where both `A` and `B` are **balanced** strings, or
- It can be written as `[C]`, where `C` is a **balanced** string.

You may swap the brackets at **any** two indices **any** number of times.

Return *the **minimum** number of swaps to make* `s` ***balanced***.

## Examples

### Example 1:

`Input: s = "][]["`

`Output: 1`

#### Explanation:

- You can make the string balanced by swapping index 0 with index 3.
- The resulting string is "[[]]".

### Example 2:

`Input: s = "]]][[["`

`Output: 2`

#### Explanation:

- You can do the following to make the string balanced:
  - Swap index 0 with index 4. s = "[]][][".
  - Swap index 1 with index 5. s = "[[][]]".
- The resulting string is "[[][]]".

### Example 3:

`Input: s = "[]"`

`Output: 0`

#### Explanation:

The string is already balanced.

## Constraints

- `n == s.length`
- `2 <= n <= 10^6`
- `n` is even.
- `s[i]` is either `'['` or `']'`.
- The number of opening brackets `'['` equals `n / 2`, and the number of closing brackets `']'` equals `n / 2`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        depth, ans = 0, 0
        for char in s:
            if char == '[':
                depth += 1
            else:
                if not depth:
                    ans += 1
                    depth += 1
                    continue
                depth -= 1

        return ans
```

## Brief Explanation
Greedy approach: we track the depth[^1] of the string. When we find a `']'` while the depth is negative, we flip it with some `'['` out there. Which one? It doesn't matter; well, technically the closest available to the end, as the hints suggest. We simulate this by increasing the current depth counter by 1 and adding one to the answer, since this is an operation.

[^1] The depth concept has been largely explained throughout this project.

## Runtime
135 ms | Beats 86.13% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
24.84 MB | Beats 98.18% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description)
