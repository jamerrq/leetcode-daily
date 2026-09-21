# [3498. Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string/description/)

**Level**: <span style="color:cyan">Easy</span>

Given a string `s`, calculate its reverse degree.

The reverse degree is calculated as follows:

For each character, multiply its position in the reversed alphabet (`'a'`= 26, `'b'`= 25, ..., `'z'`= 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.
Return the reverse degree of `s`.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            index = -ord(s[i]) + 123
            ans += (i + 1) * index
        return ans
```

## Brief Explanation

Pretty self explanatory problem to solve.

## Runtime

7 ms | Beats 69.58% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.12 MB | Beats 87.18% ![clapping_hands](../../lib/clapping_hands.svg)


## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/reverse-degree-of-a-string/description/)