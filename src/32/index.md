# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

**Level**: <span style="color:red">Hard</span>

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses substring[^1]* .

[^1]: A substring is a contiguous non-empty sequence of characters within a string.

## Examples

### Example 1:
- Input: `s = "(()"`
- Output: `2`

Explanation: The longest valid parentheses substring is `"()"`.

### Example 2:
- Input: `s = ")()())"`
- Output: `4`

Explanation: The longest valid parentheses substring is `"()()"`.

### Example 3:
- Input: `s = ""`
- Output: `0`

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('`, or `')'`.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
```

## Brief Explanation

This is quite similar to the problem of checking if a string is a VPS (check [20. Valid Parentheses](../20/index.md)). In fact the algorithm is almost the same, with the tweak of adding a sentinel to the stack, starting with `-1`, that helps to calculate the length of the current valid sequence.

This stack holds the indexes of the `(` characters that haven't been matched yet, plus the sentinel at the bottom, with start value `-1`, which means before the string starts.

When a `)` pops the last item and the stack is empty, that `)` has no match. Nothing valid can extend across it, so its index becomes the new boundary.
Otherwise, after the pop, the top of the stack is the position just before the valid substring that ends at `i`. So `i - stack[-1]` is its length.

## Runtime
11 ms | Beats 44.67%

## Memory
20.51 MB | Beats 36.23%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/longest-valid-parentheses)
