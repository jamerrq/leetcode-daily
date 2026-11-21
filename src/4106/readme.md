# [4106. Find Mismatched Segments Between Two Strings](https://leetcode.com/problems/find-mismatched-segments-between-two-strings/description)

**Level**: <span style="color:yellow">Medium</span>

You are given two strings `s1` and `s2` of the same length.

A **mismatched segment** is a **maximal contiguous** range of indices where the characters of `s1` and `s2` differ at every index.

Return a 2D array containing `[sub1, sub2]` for each mismatched segment, where `sub1` and `sub2` are the corresponding **substrings** from `s1` and `s2`, respectively. Return the segments in **increasing** order of their starting indices. If there are no mismatched segments, return an empty array.

## Examples

### Example 1:

`Input: s1 = "earth", s2 = "empty"`

`Output: [["ar","mp"],["h","y"]]`

#### Explanation:

- The characters at indices 1 and 2 differ, forming the mismatched segment `["ar","mp"]`.
- The characters at index 4 differ, forming the mismatched segment `["h","y"]`.

### Example 2:

`Input: s1 = "action", s2 = "nation"`

`Output: [["ac","na"]]`

#### Explanation:

The characters at indices 0 and 1 differ, forming the mismatched segment `["ac","na"]`. All remaining characters are equal in both strings.

### Example 3:

`Input: s1 = "hot", s2 = "hot"`

`Output: []`

#### Explanation:

The two strings are identical, so there are no mismatched segments.

## Constraints

- `1 <= s1.length == s2.length <= 100`
- `s1` and `s2` consist of lowercase English letters.

## My Solution
[index.py](./index.py)

```python
class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        n = len(s1)
        segments: list[list[str]] = []
        index = 0
        cs1, cs2 = "", ""
        while index < n:
            s1c, s2c = s1[index], s2[index]
            if s1c != s2c:
                cs1 += s1c
                cs2 += s2c
            else:
                if cs1:
                    segments.append([cs1, cs2])
                cs1 = ""
                cs2 = ""

            index += 1

        if cs1:
            segments.append([cs1, cs2])

        return segments
```

## Runtime
2 ms | Beats 69.12% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
19.20 MB | Beats 63.43% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/find-mismatched-segments-between-two-strings/description)
