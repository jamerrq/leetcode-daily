# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description)

**Level**: <span style="color:cyan">Easy</span>

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1:

`Input: s = "()"`

`Output: true`

### Example 2:

`Input: s = "()[]{}"`

`Output: true`

### Example 3:

`Input: s = "(]"`

`Output: false`

### Example 4:

`Input: s = "([])"`

`Output: true`

### Example 5:

`Input: s = "([)]"`

`Output: false`

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_d = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or open_d.get(stack.pop()) != char:
                    return False

        return not stack
```

## Brief Explanation

This is a well-known problem that is solved with a stack. The algorithm is very simple and self-explanatory: if we encounter an open character, i.e. `(`, `[` or `{`, we push it onto the stack. If we find a closing character, we pop from the stack and verify that it matches. That's all.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.17 MB | Beats 91.65% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/valid-parentheses/description)
