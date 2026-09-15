# [3483. Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11)

You are given an array of digits called `digits`. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

**Note**: Each copy of a digit can only be used once per number, and there may not be leading zeros.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()
        n = len(digits)
        for i in range(n):
            first = digits[i]
            if not first:
                continue
            #
            for j in range(n):
                if j == i:
                    continue
                second = digits[j]
                #
                for k in range(n):
                    if k == j or k == i:
                        continue
                    third = digits[k]
                    if third % 2:
                        continue
                    candidate = first * 100 + second * 10 + third
                    s.add(candidate)

        return len(s)
```

## Brief Explanation

Due to the constraints, brute force is not a big deal, so this is the way.

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11)