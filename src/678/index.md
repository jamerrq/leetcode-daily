# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description)

**Level**: <span style="color:yellow">Medium</span>

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid.

The following rules define a valid string:

- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

## Examples

### Example 1:

`Input: s = "()"`

`Output: true`

### Example 2:

`Input: s = "(*)"`

`Output: true`

### Example 3:

`Input: s = "(*))"`

`Output: true`

### Example 4:

`Input: s = "("`

`Output: false`

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack, stars_stack = [], []
        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                stars_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif stars_stack:
                    stars_stack.pop()
                else:
                    return False

        while open_stack and stars_stack:
            if open_stack.pop() > stars_stack.pop():
                return False

        return not open_stack
```

## Brief Explanation

Greedy approach: we create two stacks, one for the open parentheses and another one for the stars. Whenever we find one of these, we push its index onto its stack. If we find a closing one, we check the stacks: if both are empty, we return `False`, since we reached a negative depth. If not, we prefer popping from the open stack, and if it is empty, we pop from the stars stack.

At the end, if we don't have any elements in the open stack, we return `True`. Otherwise, we pop from the stars stack to match, keeping in mind that since we were pushing indexes in order, they remain ordered, and if we pop some index from the open stack that comes after a star, it means that it couldn't be balanced, so in this case we return `False`.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.32 MB | Beats 31.35%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/valid-parenthesis-string/description)
