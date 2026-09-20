class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # center at (0, 0)
        x1 -= xCenter; x2 -= xCenter
        y1 -= yCenter; y2 -= yCenter

        # parabola f(y) = set_x² + y², vertex at y = 0
        set_x = max(x1, min(0, x2))
        y = max(y1, min(0, y2))

        return set_x * set_x + y * y <= radius * radius
