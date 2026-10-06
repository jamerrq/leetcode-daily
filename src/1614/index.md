# [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description)

**Level**: <span style="color:cyan">Easy</span>

Given a valid parentheses string `s`, return the nesting depth of `s`. The nesting depth is the maximum number of nested parentheses.

## Examples

### Example 1:

`Input: s = "(1+(2*3)+((8)/4))+1"`

`Output: 3`

Explanation: Digit 8 is inside of 3 nested parentheses in the string.

### Example 2:

`Input: s = "(1)+((2))+(((3)))"`

`Output: 3`

Explanation: Digit 3 is inside of 3 nested parentheses in the string.

### Example 3:

`Input: s = "()(())((()()))"`

`Output: 3`

## Constraints

- `1 <= s.length <= 100`
- `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
- It is guaranteed that parentheses expression `s` is a VPS.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth, depth = 0, 0
        for char in s:
            if char == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            elif char == ')':
                depth -= 1
        return maxDepth
```

## Brief Explanation
The concept of depth at this point is quite intuitive and simple: the amount of open parentheses that have not been closed.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.28 MB | Beats 49.17% ![clapping_hands](../../lib/clapping_hands.svg)

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description)
