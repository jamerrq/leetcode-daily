class Solution:
    def countCommas(self, n: int) -> int:
        mm = 0
        if n == 1e15:
            mm = 5

        zz = max(0, min(1e15 - 1, n) - 1e12 + 1)
        yy = max(0, min(1e12 - 1, n) - 1e9 + 1)
        xx = max(0, min(1e9 - 1, n) - 1e6 + 1)
        vv = max(0, min(1e6 - 1, n) - 1e3 + 1)

        return int(zz * 4 + yy * 3 + xx * 2 + vv + mm)
