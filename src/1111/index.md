# [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description)

**Level**: <span style="color:yellow">Medium</span>

A string is a valid parentheses string (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

- It is the empty string, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or
- It can be written as `(A)`, where `A` is a VPS.

We can similarly define the *nesting depth* `depth(S)` of any VPS S as follows:

- `depth("") = 0`
- `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's
- `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.

For example, `""`, `"()()"`, and `"()(()())"` are VPS's (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPS's.

Given a VPS `seq`, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPS's (and `A.length + B.length = seq.length`). The subsequences may not necessarily be contiguous.
t
For example, for the sequence `123456789`, one possible split is:

- `A = {1, 3, 5, 7, 9}`,

- `B = {2, 4, 6, 8}`.

This corresponds to the output `[0, 1, 0, 1, 0, 1, 0, 1, 0]`  where `0` indicates membership in `A` and `1` indicates membership in `B`.

Now choose any such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`:  `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`.  Note that even though multiple answers may exist, you may return any of them.

## Examples

### Example 1:

`Input: seq = "(()())"`

`Output: [0,1,1,1,1,0]`

### Example 2:

`Input: seq = "()(())()"`

`Output: [0,0,0,1,1,0,1,1]`

## Constraints

- `1 <= seq.size <= 10000`

## My Solution

[index.py](./index.py)

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)

        for i, elem in enumerate(seq):
            if elem == '(' and i % 2 or elem == ')' and not i % 2:
                ans[i] = 1

        return ans
```

## Brief Explanation

Just give half of each group of parentheses to each subsequence.
How? We can notice that each character changes the depth by 1, so, the parity of the index is the same as the parity of the depth.

For example, for the sequence `"(())(())"` has the depth sequence `121010` which is a mix of even and odd numbers, this applies for every sequence.

Now check the parity of the indexes for each open parenthesis with its closing one. They are always in a different parity:

```
(())(())
0  3
 12
    4  7
     56
```

Why? In the base case it's clear to see `() -> 01` in any other case `(A)` the length of `A` will be always even since it is a valid sequence. In consequence, its sum with `1` will be odd, which is the position of the closing parenthesis.

At the same time, alternating groups alternate parity as well.

So assigning a group for the open parentheses that land at indexes with odd pairity plus the closing ones on even indexes is a valid sequence and aim to split the sequence in half of the overall depth.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.16 MB | Beats 98.24% ![clapping_hands](../../lib/clapping_hands.svg)

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings)