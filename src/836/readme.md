# [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)

**Level**: <span style="color:cyan">Easy</span>

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true` if they overlap, otherwise return `false`.

## Examples

### Example 1:

`Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]`

`Output: true`

#### Explanation:

The rectangles overlap in the region with corners at `(1,1)`, `(2,1)`, `(1,2)`, and `(2,2)`.

This region has positive area, so the rectangles overlap.

### Example 2:

`Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]`

`Output: false`

#### Explanation:

The rectangles share the vertical edge where `x = 1`, but they do not have any common interior region.

Since their intersection has zero area, the rectangles do not overlap.

### Example 3:

`Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]`

`Output: false`

#### Explanation:

The rectangles are completely separate. Rectangle `rec1` ends at `x = 1` and `y = 1`, while `rec2` starts at `x = 2` and `y = 2`.

Therefore, they have no common points and do not overlap.

## Constraints

- `rec1.length == 4`
- `rec2.length == 4`
- `-10^9 <= rec1[i], rec2[i] <= 10^9`
- `rec1` and `rec2` represent a valid rectangle with a non-zero area.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        idxs = [0, 0, 2, 2]
        idys = [1, 3, 3, 1]
        #
        for i in range(4):
            cx = rec1[idxs[i]]
            cy = rec1[idys[i]]
            if rec2[0] < cx < rec2[2] and rec2[1] < cy < rec2[3]:
                return True
            #
            dx = rec2[idxs[i]]
            dy = rec2[idys[i]]
            if rec1[0] < dx < rec1[2] and rec1[1] < dy < rec1[3]:
                return True

        if rec1[0] < (rec2[2] + rec2[0]) / 2 < rec1[2] and \
            rec1[1] < (rec2[3] + rec2[1]) / 2 < rec1[3]:
            return True

        if rec2[0] < (rec1[2] + rec1[0]) / 2 < rec2[2] and \
            rec2[1] < (rec1[3] + rec1[1]) / 2 < rec2[3]:
            return True

        return False
```

## Brief Explanation

It can be shown that if two rectangles overlap, at least one corner from one
rectangle will be inside the other, or the middle point.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.31 MB | Beats 21.16%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)