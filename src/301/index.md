# [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/description)

**Level**: <span style="color:red">Hard</span>

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return *a list of **unique strings** that are valid with the minimum number of removals*. You may return the answer in **any order**.

## Examples

### Example 1:

`Input: s = "()())()"`

`Output: ["(())()","()()()"]`

### Example 2:

`Input: s = "(a)())()"`

`Output: ["(a())()","(a)()()"]`

### Example 3:

`Input: s = ")("`

`Output: [""]`

## Constraints

- `1 <= s.length <= 25`
- `s` consists of lowercase English letters and parentheses `'('` and `')'`.
- There will be at most `20` parentheses in `s`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    @staticmethod
    def isValid(s: str, ignore_set: set[int]):
        depth = 0
        for i, char in enumerate(s):
            if i in ignore_set:
                continue
            if char == '(':
                depth += 1
            elif char == ')':
                if not depth:
                    return False
                depth -= 1

        return not depth

    @staticmethod
    def isValidAfterChanges(
        s:str,
        index_stack: list[int],        # indexes that can be removed '(' or ')'
        remaining:int,                 # how many left to remove
        candidates:set[str],           # to store the candidates
        ignore_set:set[int],           # indexes that won't count
        ) -> bool:
        if not remaining:
            n = len(s)
            veredict = Solution.isValid(s, ignore_set)
            if veredict:
                s_cand = "".join(s[i] for i in range(n) if i not in ignore_set)
                candidates.add(s_cand)
            return veredict
        if not index_stack:
            return False

        indexes_copy = [index for index in index_stack]
        index_to_ignore = indexes_copy.pop()
        ignore_set_copy = set(x for x in ignore_set)
        ignore_set_copy.add(index_to_ignore)

        # option 1, to change
        option1 = Solution.isValidAfterChanges(
            s,
            indexes_copy,
            remaining - 1,
            candidates,
            ignore_set_copy,
        )
        # option 2, to pass
        option2 = Solution.isValidAfterChanges(
            s,
            indexes_copy,
            remaining,
            candidates,
            ignore_set,
        )

        return option1 or option2

    def removeInvalidParentheses(self, s: str) -> list[str]:
        depth, changes = 0, 0
        open_stack, close_stack = [], []
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
                open_stack.append(i)
            elif char == ')':
                if not depth:
                    changes += 1
                else:
                    depth -= 1
                close_stack.append(i)

        choosen_stack = []
        if depth and not changes:
            choosen_stack = [index for index in open_stack]
        elif changes and not depth:
            choosen_stack = [index for index in close_stack]
        else:
            choosen_stack = [index for index in open_stack + close_stack]

        choosen_stack.sort()

        candidates = set()
        ignore_set = set()
        remaining = depth + changes
        self.isValidAfterChanges(
            s, choosen_stack, remaining, candidates, ignore_set
        )

        return list(candidates)
```

## Brief Explanation
I would admit I'm not proud of this solution. There's a lot of room for improvements and I would eventually (hopefully) implement all of them.
For now, with recursion we try removing all the possible characters from the minimum, which is basically the solution for this other [problem](../1541/index.md).

## Runtime
3767 ms | Beats 5.01%

## Memory
19.38 MB | Beats 81.71%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/remove-invalid-parentheses/description)
