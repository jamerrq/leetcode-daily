# [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

## My Solution

[index.py](./index.py)

```python
# runtime: 3ms
# memory: 19.4MB
class Solution:
    def reverseParentheses(self, s: str) -> str:
        depths = [0] * (len(s) // 2)
        depth = 0
        intervals = []
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
                depths[depth] = i
            elif char == ')':
                left = depths[depth]
                intervals.append((left, i + 1))
                depth -= 1
        chars = list(s)
        for interval in intervals:
            left, right = interval
            chars[left:right] = chars[left:right][::-1]
        return "".join(chars).replace("(", "").replace(")", "")
```

## Brief Explanation
Consider the depth at some position in the string to be the count of the left parentheses to its left, minus the right ones.
My first approach was to iterate through the string while copying the characters; if we find an open parenthesis, we remember its position. To achieve this, we can have an array depths where `depths[i]` is the position where the `depth = i` starts. Since two groups at the same depth can't be open at the same time, each slot in `depths` is only overwritten after its group has closed.
When we reach a closing parenthesis `)` we reverse the string between the current position and the index saved for the current depth.

However, there is a better approach that doesn't require reversing parts of the string at each nested range: the wormhole approach.

That is, first we iterate through the string: when we find an open parenthesis, we save the position in a stack `opened`; when we find a closing one, we pop from `opened` and create a bidirectional connection between the popped index and the current one.

Then we iterate a second time; if the current position is a parenthesis, we travel to the other end of the bidirectional connection and change the direction of our loop.
Here, direction is an int that is `1` if we travel from left to right and `-1` if it is the other way.

The improved version code:

```python
# runtime: 0ms
# memory: 19.4MB
class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        wormhole = {}
        for i, char in enumerate(s):
            if char == '(':
                opened.append(i)
            elif char == ')':
                open_index = opened.pop()
                wormhole[open_index] = i
                wormhole[i] = open_index
        curr_index = 0
        direction = 1
        ans = ""
        while curr_index < len(s):
            char = s[curr_index]
            if char == '(' or char == ')':
                curr_index = wormhole.get(curr_index, -1)
                direction *= -1
            else:
                ans += s[curr_index]
            curr_index += direction

        return ans
```

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.4 MB | Beats 32.65%


## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description)