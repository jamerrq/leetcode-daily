# [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description)

**Level**: <span style="color:yellow">Medium</span>

Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is **balanced** if:

- Any left parenthesis `'('` must have a corresponding two consecutive right parentheses `'))'`.
- Left parenthesis `'('` must go before the corresponding two consecutive right parentheses `'))'`.

In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing parenthesis.

- For example, `"())"`, `"())(())))"` and `"(())())))"` are balanced, `")()"`, `"()))"` and `"(()))"` are not balanced.

You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return *the minimum number of insertions* needed to make `s` balanced.

## Examples

### Example 1:

`Input: s = "(()))"`

`Output: 1`

#### Explanation:

The second `'('` has two matching `'))'`, but the first `'('` has only `')'` matching. We need to add one more `')'` at the end of the string to be `"(())))"` which is balanced.

### Example 2:

`Input: s = "())"`

`Output: 0`

#### Explanation:

The string is already balanced.

### Example 3:

`Input: s = "))())("`

`Output: 3`

#### Explanation:

Add `'('` to match the first `'))'`, add `'))'` to match the last `'('`.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of `'('` and `')'` only.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        left, ans, index, n = 0, 0, 0, len(s)

        while index < n:
            char = s[index]

            if char == '(':
                left += 1
                index += 1
                continue

            if not left:
                ans += 1
            else:
                left -= 1

            next_char = s[index + 1] if index != n - 1 else ""
            if next_char == ')':
                index += 2
                continue

            ans += 1
            index += 1

        return ans + 2 * left
```

## Brief Explanation

We can calculate this greedily by adding one if we find a closing parenthesis
without any available to match and the next character being another closing one,
or 2 if the next character is the open parenthesis or there is no next one. At
the end we sum 2 for each open parenthesis that is left unmatched.

## Runtime
71 ms | Beats 57.99% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.87 MB | Beats 49.05%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description)
