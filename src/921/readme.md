# [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description)

**Level**: <span style="color:yellow">Medium</span>

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as (`A`), where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be `"())))"`.

Return the minimum number of moves required to make `s` valid.

## Examples

### Example 1:

`Input: s = "())"`

`Output: 1`

### Example 2:

`Input: s = "((("`

`Output: 3`

## Constraints

- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth, ans = 0, 0
        for char in s:
            if char == ')':
                if not depth:
                    ans += 1
                    continue
                depth -= 1
            else:
                depth += 1

        return ans + depth
```

## Brief Explanation

Simple, quite simple.

We track the depth of the string, if we reach some negative depth, we need to
add an open parenthesis to keep it balanced. At the end we need to add the depth
that's left to reach the depth 0.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.15 MB | Beats 86.35% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description)
