# [1401. Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

**Level**: <span style="color:yellow">Medium</span>

You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of the top-right corner of the rectangle.

Return `true` if the circle and rectangle are overlapped, otherwise return `false`. In other words, check if there is any point `(xi, yi)` that belongs to the circle and the rectangle at the same time.

## Examples

### Example 1:

![](https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png)

`Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1`

`Output: true`

#### Explanation:

Circle and rectangle share the point (1,0).

### Example 2:

`Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1`

`Output: false`

### Example 3:

![](https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png)

`Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1`

`Output: true`

## Constraints

- `1 <= radius <= 2000`
- `-10^4 <= xCenter, yCenter <= 10^4`
- `-10^4 <= x1 < x2 <= 10^4`
- `-10^4 <= y1 < y2 <= 10^4`

## My Solution

[index.py](./index.py)

```python
class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # center at (0, 0)
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter

        # parabola f(y) = set_x² + y², vertex at y = 0
        set_x = max(x1, min(0, x2))
        y = max(y1, min(0, y2))

        return set_x * set_x + y * y <= radius * radius
```

## Brief Explanation

There are many ways to solve this. It was a very good mental exercise to think
about them.

My preferred one was this: if we fix one side of the rectangle (in this case,
the x closest to the circle), we can check the distance from the points of this
line to the center of the circle. If any of the points is closer than the
radius, we conclude they overlap.

As this distance draws a parabola with its vertex at y = 0, we can take the y
closest to zero (zero itself, if it's in range). That will be the closest point
of the rectangle to the circle, so checking the distance to this point is
enough.

## Runtime

0 ms | Beats 100% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.30 MB | Beats 86.06% ![clapping_hands](../../lib/clapping_hands.svg)

## Submission Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/circle-and-rectangle-overlapping)
