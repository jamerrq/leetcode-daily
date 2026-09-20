class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xMin = max(x1, xCenter - radius)
        xMax = min(x2, xCenter + radius)
        yMin = max(y1, yCenter - radius)
        yMax = min(y2, yCenter + radius)

        # no possible range
        if xMin > xMax or yMin > yMax:
            return False

        # for convenience, let's move the circle center to (0, 0)
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter

        xMin = max(x1, -radius)
        xMax = min(x2, radius)
        yMin = max(y1, -radius)
        yMax = min(y2, radius)

        dxMin = (xMin ** 2 + yMin ** 2) ** 0.5
        dxMax = (xMax ** 2 + yMin ** 2) ** 0.5

        # fix the axis on whichever side is closest
        set_x = xMin
        if dxMin > dxMax:
            set_x = xMax

        for yi in range(yMin, yMax):
            di = (set_x ** 2 + yi ** 2) ** 0.5
            if di <= radius:
                return True

        for xi in range(xMin, xMax):
            di = (xi ** 2 + yMin ** 2) ** 0.5
            if di <= radius:
                return True

        return False

s = Solution()
radius = 11
xCenter = 3
yCenter = -3
x1 = 10
y1 = -13
x2 = 15
y2 = -11
print(s.checkOverlap(radius,xCenter,yCenter,x1,y1,x2,y2))
