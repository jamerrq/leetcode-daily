# [1441. Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/description)

**Level**: <span style="color:yellow">Medium</span>

You are given an integer array `target` and an integer `n`.

You have an empty stack with the two following operations:

- **`"Push"`**: pushes an integer to the top of the stack.
- **`"Pop"`**: removes the integer on the top of the stack.

You also have a stream of the integers in the range `[1, n]`.

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to `target`. You should follow the following rules:

- If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
- If the stack is not empty, pop the integer at the top of the stack.
- If, at any moment, the elements in the stack (from the bottom to the top) are equal to `target`, do not read new integers from the stream and do not do more operations on the stack.

Return *the stack operations needed to build* `target` following the mentioned rules. If there are multiple valid answers, return **any of them**.

## Examples

### Example 1:

`Input: target = [1,3], n = 3`

`Output: ["Push","Push","Pop","Push"]`

#### Explanation:

- Initially the stack s is empty. The last element is the top of the stack.
- Read 1 from the stream and push it to the stack. s = [1].
- Read 2 from the stream and push it to the stack. s = [1,2].
- Pop the integer on the top of the stack. s = [1].
- Read 3 from the stream and push it to the stack. s = [1,3].

### Example 2:

`Input: target = [1,2,3], n = 3`

`Output: ["Push","Push","Push"]`

#### Explanation:

- Initially the stack s is empty. The last element is the top of the stack.
- Read 1 from the stream and push it to the stack. s = [1].
- Read 2 from the stream and push it to the stack. s = [1,2].
- Read 3 from the stream and push it to the stack. s = [1,2,3].

### Example 3:

`Input: target = [1,2], n = 4`

`Output: ["Push","Push"]`

#### Explanation:

- Initially the stack s is empty. The last element is the top of the stack.
- Read 1 from the stream and push it to the stack. s = [1].
- Read 2 from the stream and push it to the stack. s = [1,2].
- Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
- The answers that read integer 3 from the stream are not accepted.

## Constraints

- `1 <= target.length <= 100`
- `1 <= n <= 100`
- `1 <= target[i] <= n`
- `target` is strictly increasing.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans, i, index = [], 1, 0
        while i <= target[-1]:
            if target[index] == i:
                ans.append("Push")
                index += 1
            else:
                ans.append("Push")
                ans.append("Pop")
            i += 1

        return ans
```

## Brief Explanation

Since the requested `target` array is in increasing order, we can do this
greedily, inserting all elements and popping those which we don't need.

## Runtime
0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.21 MB | Beats 67.52% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/build-an-array-with-stack-operations/description)
