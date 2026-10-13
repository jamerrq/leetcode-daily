# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

## Examples

### Example 1:

`Input: tokens = ["2","1","+","3","*"]`

`Output: 9`

#### Explanation:

((2 + 1) * 3) = 9

### Example 2:

`Input: tokens = ["4","13","5","/","+"]`

`Output: 6`

#### Explanation:

(4 + (13 / 5)) = 6

### Example 3:

`Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`

`Output: 22`

#### Explanation:

```text
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                op = token
                B, A = stack.pop(), stack.pop()
                C = A + B
                match op:
                    case '-':
                        C = A - B
                    case '*':
                        C = A * B
                    case '/':
                        C = int(A / B)
                stack.append(C)

        return stack[0]
```

## Brief Explanation

Spot the pattern: an operation character appears after two numbers.
We can have a stack that saves the numbers as we encounter digits; otherwise, we pop the last two and execute the operation.
This is an algorithm known as shunting yard:
https://en.wikipedia.org/wiki/Shunting_yard_algorithm

## Runtime
3 ms | Beats 55.27% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
20.81 MB | Beats 11.03%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/evaluate-reverse-polish-notation/description)
