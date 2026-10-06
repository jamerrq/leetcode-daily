# [1401. Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

**Level**: <span style="color:yellow">Medium</span>

You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of the top-right corner of the rectangle.

Return `true` if the circle and rectangle are overlapped, otherwise return `false`. In other words, check if there is any point `(xi, yi)` that belongs to the circle and the rectangle at the same time.

## My Solution

[index.py](./index.py)

```python
class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # center at (0, 0)
        x1 -= xCenter; x2 -= xCenter
        y1 -= yCenter; y2 -= yCenter

        # parabola f(y) = set_x² + y², vertex at y = 0
        set_x = max(x1, min(0, x2))
        y = max(y1, min(0, y2))

        return set_x * set_x + y * y <= radius * radius
```

## Brief Explanation
There are many ways to solve this. It was a very good mental exercise to think about them.

My preferred one was this: if we fix one side of the rectangle (in this case, the x closest to the circle), we can check
the distance from the points of this line to the center of the circle. If any of the points is closer than the radius, we conclude they overlap.

As this distance draws a parabola with its vertex at y = 0, we can take the y closest to zero (zero itself, if it's in range). That will be the closest point of the rectangle to the circle, so checking the distance to this point is enough.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.30 MB | Beats 86.06% ![clapping_hands](../../lib/clapping_hands.svg)

## Submission Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/circle-and-rectangle-overlapping)
