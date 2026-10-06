# [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/description)

**Level**: <span style="color:yellow">Medium</span>

Given a balanced parentheses string `s`, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

- `"()"` has score 1.
- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

## Examples

### Example 1:

`Input: s = "()"`

`Output: 1`

### Example 2:

`Input: s = "(())"`

`Output: 2`

### Example 3:

`Input: s = "()()"`

`Output: 2`

## Constraints

- `2 <= s.length <= 50`
- `s` consists of only `'('` and `')'`.
- `s` is a balanced parentheses string.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        max_depth, depth = len(s) // 2, 0
        groups = [0] * (max_depth + 1)

        for char in s:
            if char == '(':
                depth += 1
                groups[depth] = 0
            else:
                depth -= 1
                prev = groups[depth + 1]
                groups[depth] += 2 * prev if prev else 1

        return groups[0]
```

### Another Approach (Feedback Agent)

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth, ans = 0, 0

        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                prev = s[i - 1]
                if prev == '(':
                    ans += 1 << depth

        return ans
```

## Brief Explanation

Consider this algorithm: if we find an open parenthesis, we increase the depth count and clear the `groups[depth]` position for what's coming inside.
Once we reach a closing parenthesis, we check what we counted inside and multiply it by `2`, or take `1` if there was nothing inside, and add the result to `groups[depth]`.

### Another approach

Thanks to the agent review for this idea.

Notice that only the `()` substrings (let's call them "cores") add to the final answer. Other cases are either a core wrapped in nested parentheses or a sum of terms. So we can iterate through the string tracking the depth (same definition as in the section above), and whenever we find a core, we add `2^depth` to the final answer.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.08 MB | Beats 97.89% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/score-of-parentheses/description)
