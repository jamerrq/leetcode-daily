# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description)

**Level**: <span style="color:yellow">Medium</span>

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

### Example 1:

`Input: n = 3`

`Output: ["((()))","(()())","(())()","()(())","()()()"]`

### Example 2:

`Input: n = 1`

`Output: ["()"]`

## Constraints

- `1 <= n <= 8`

## My Solution
[index.py](./index.py)

```python
class Solution:
    def __init__(self):
        self.mem: dict[(int, list[str])] = {0: [""]}

    def generateParenthesis(self, n: int) -> list[str]:
        if self.mem.get(n):
            return self.mem[n]
        s_n = []
        for i in range(n):
            A = self.generateParenthesis(i)
            B = self.generateParenthesis(n - i - 1)
            for a in A:
                for b in B:
                    s_n.append(f"({a}){b}")

        self.mem[n] = s_n
        return s_n
```

## Another approach (backtracking)

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(left, right, curr=""):

            if right == n:
                ans.append(curr)
                return

            if left < n:
                backtrack(left + 1, right, f"{curr}(")
            if right < left:
                backtrack(left, right + 1, f"{curr})")

        backtrack(0, 0, "")
        return ans
```

## Brief Explanation

Every parentheses group can be defined as:

$S_n = \{\ (a)\,b \ :\ a \in S_i,\ b \in S_{n-1-i},\ 0 \le i \le n-1 \ \}$

where $i$ is the number of pairs inside the first group and $n-1-i$ is the number of pairs after it.

With the base case $S_0=[""]$ we have all the ingredients for our recursion.

### The backtrack approach

Consider the decision in each node to add an open parenthesis or a closing one.
When a path reaches `n` closing parentheses (so `2n` characters in total), we consider it valid. To prune invalid paths, we only add an open parenthesis while there are fewer than `n` of them, and a closing one while there are fewer closing ones than open ones.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.2 MB | Beats 99.51% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/generate-parentheses/description)
