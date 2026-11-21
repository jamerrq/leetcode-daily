class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [0] * n
        cols = [0] * m
        servers: list[tuple[int, int]] = []
        for row in range(n):
            for col in range(m):
                if grid[row][col]:
                    rows[row] += 1
                    cols[col] += 1
                    servers.append((row, col))

        ans = 0
        for row, col in servers:
            if rows[row] > 1 or cols[col] > 1:
                ans += 1

        return ans
