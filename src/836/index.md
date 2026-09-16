# [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true` if they overlap, otherwise return `false`.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check every corner
        # corner 1
        c1_x, c1_y = rec1[0], rec1[1]
        c2_x, c2_y = rec1[0], rec1[3]
        c3_x, c3_y = rec1[2], rec1[3]
        c4_x, c4_y = rec1[2], rec1[1]
        # add middle point
        c5_x, c5_y = (rec1[0] + rec1[2]) / 2, (rec1[1] + rec1[3]) / 2
        #
        d1_x, d1_y = rec2[0], rec2[1]
        d2_x, d2_y = rec2[0], rec2[3]
        d3_x, d3_y = rec2[2], rec2[3]
        d4_x, d4_y = rec2[2], rec2[1]
        # add middle point
        d5_x, d5_y = (rec2[0] + rec2[2]) / 2, (rec2[1] + rec2[3]) / 2
        #
        cxs = [c1_x, c2_x, c3_x, c4_x, c5_x]
        cys = [c1_y, c2_y, c3_y, c4_y, c5_y]
        dxs = [d1_x, d2_x, d3_x, d4_x, d5_x]
        dys = [d1_y, d2_y, d3_y, d4_y, d5_y]
        #
        for i in range(5):
            cx = cxs[i]
            cy = cys[i]
            if d1_x <= cx <= d3_x and d1_y <= cy <= d3_y:
                A = (cx - d1_x) * (cy - d1_y)
                B = (d3_x - cx) * (d3_y - cy)
                if A * B:
                    return True
            #
            dx = dxs[i]
            dy = dys[i]
            if c1_x <= dx <= c3_x and c1_y <= dy <= c3_y:
                A = (dx - c1_x) * (dy - c1_y)
                B = (c3_x - dx) * (c3_y - dy)
                if A * B:
                    return True

        return False

```

## Brief Explanation

It can be shown that if two rectangles overlap, at least one corner from one rectangle will be inside the other, or the middle point.
Having that in mind, the next step is to measure the area of the rectangles formed by the point inside and two corners of the other rectangle such that they don't have the same x or y coordinate, if both areas are non zero, we can say the rectangles overlap.

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/rectangle-overlap/description/?envType=daily-question&envId=2026-09-15)