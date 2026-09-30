# [1807. Evaluate the Bracket Pairs of a String](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a string `s` that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string `"(name)is(age)yearsold"`, there are two bracket pairs that contain the keys `"name"` and `"age"`.
You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each $knowledge[i] = [key_i, value_i]$ indicates that key $key_i$ has a value of $value_i$.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key $key_i$, you will:

Replace $key_i$ and the bracket pair with the key's corresponding $value_i$.
If you do not know the value of the key, you will replace $key_i$ and the bracket pair with a question mark `"?"` (without the quotation marks).
Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return the resulting string after evaluating all of the bracket pairs.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mem = dict(knowledge)
        n = len(s)
        ans = []
        curr = ""
        for i in range(n):
            if s[i] == '(':
               ans.append(curr)
               curr = ""
            elif s[i] == ')':
                ans.append(mem.get(curr, '?'))
                curr = ""
            else:
                curr += s[i]
        ans.append(curr)
        return ''.join(ans)
```

## Brief Explanation

I feel like this problem should be tagged as easy, since there are no nested loops involved. The description just tells you directly what to do, and solving it takes no real mental effort.

## Runtime

55 ms | Beats 45.17%

## Memory

97.82 MB | Beats 97.82% ![clapping_hands](../../lib/clapping_hands.svg)

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string)