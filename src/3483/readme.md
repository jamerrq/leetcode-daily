# [3483. Unique 3-Digit Even Numbers](https://leetcode.com/problems/unique-3-digit-even-numbers)

**Level**: <span style="color:cyan">Easy</span>

You are given an array of digits called `digits`. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

**Note**: Each copy of a digit can only be used once per number, and there may not be leading zeros.

## Examples

### Example 1:

`Input: digits = [1,2,3,4]`

`Output: 12`

#### Explanation:

The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

### Example 2:

`Input: digits = [0,2,2]`

`Output: 2`

#### Explanation:

The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

### Example 3:

`Input: digits = [6,6,6]`

`Output: 1`

#### Explanation:

Only 666 can be formed.

### Example 4:

`Input: digits = [1,3,5]`

`Output: 0`

#### Explanation:

No even 3-digit numbers can be formed.

## Constraints

- `3 <= digits.length <= 10`
- `0 <= digits[i] <= 9`

## My Solution

[index.py](./index.py) · [animation](./animation.html)

```python
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
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

### Another approach (fixed checks)

```python
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        freq = [0] * 10
        for digit in digits:
            freq[digit] += 1
        total = 0
        # last digit (units)
        for i in range(0, 9, 2):
            if not freq[i]:
                continue
            freq[i] -= 1
            subtotal = 0
            # tens
            for j in range(0, 10):
                fj = freq[j]
                if not fj:
                    continue
                # hundreds
                for k in range(1, 10):
                    fk = freq[k]
                    if not fk or (k == j and fk < 2):
                        continue
                    subtotal += 1
            total += subtotal
            freq[i] += 1
        return total
```

## Brief Explanation

Due to the constraints, brute force is not a big deal, so this is the way.

### Fixed checks approach

Another way is to store the frequency of each digit. Then we iterate over the
even digits and check if they appear at least once. If they do, we check every
possible combination for the hundreds and tens, keeping in mind that we can't
reuse the current even digit, so we temporarily subtract 1 from its count in
`freq`.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.14 MB | Beats 94.20% ![clapping_hands](../../lib/clapping_hands.svg)

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/unique-3-digit-even-numbers/)
