# [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)

**Level**: <span style="color:cyan">Easy</span>

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true` if they overlap, otherwise return `false`.

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

It can be shown that if two rectangles overlap, at least one corner from one rectangle will be inside the other, or the middle point.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.31 MB | Beats 21.16%

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)