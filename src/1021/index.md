# [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/description)

**Level**: <span style="color:cyan">Easy</span>

A valid parentheses string is either empty `""`, `"(" + A + ")"`, or `A + B`, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

- For example, `""`, `"()"`, `"(())()"`, and `"(()(()))"` are all valid parentheses strings.

A valid parentheses string `s` is primitive if it is nonempty, and there does not exist a way to split it into `s = A + B`, with `A` and `B` nonempty valid parentheses strings.

Given a valid parentheses string `s`, consider its primitive decomposition: `s = P_1 + P_2 + ... + P_k`, where `P_i` are primitive valid parentheses strings.

Return `s` *after removing the outermost parentheses of every primitive string in the primitive decomposition of* `s`.

## Examples

### Example 1:

`Input: s = "(()())(())"`

`Output: "()()()"`

#### Explanation:

- The input string is `"(()())(())"`, with primitive decomposition `"(()())" + "(())"`.
- After removing outer parentheses of each part, this is `"()()" + "()" = "()()()"`.

### Example 2:

`Input: s = "(()())(())(()(()))"`

`Output: "()()()()(())"`

#### Explanation:

- The input string is `"(()())(())(()(()))"`, with primitive decomposition `"(()())" + "(())" + "(()(()))"`.
- After removing outer parentheses of each part, this is `"()()" + "()" + "()(())" = "()()()()(())"`.

### Example 3:

`Input: s = "()()"`

`Output: ""`

#### Explanation:

- The input string is `"()()"`, with primitive decomposition `"()" + "()"`.
- After removing outer parentheses of each part, this is `"" + "" = ""`.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('` or `')'`.
- `s` is a valid parentheses string.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth, start = 0, 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
                if depth == 1:
                    start = i + 1
            else:
                depth -= 1
                if not depth:
                    ans.append(s[start:i])

        return "".join(ans)
```

## Brief Explanation
We just simply add what's inside `depth` 1.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.36 MB | Beats 32.05%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/remove-outermost-parentheses/description)
