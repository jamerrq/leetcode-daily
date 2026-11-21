# [1267. Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/description)

**Level**: <span style="color:yellow">Medium</span>

You are given a map of a server center, represented as a `m * n` integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

## Examples

### Example 1:

![](https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg)

`Input: grid = [[1,0],[0,1]]`

`Output: 0`

#### Explanation:

No servers can communicate with others.

### Example 2:

![](https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg)

`Input: grid = [[1,0],[1,1]]`

`Output: 3`

#### Explanation:

All three servers can communicate with at least one other server.

### Example 3:

![](https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg)

`Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`

`Output: 4`

#### Explanation:

The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 250`
- `1 <= n <= 250`
- `grid[i][j] == 0 or 1`

## My Solution
[index.py](./index.py)

```python
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
```

## Runtime
7 ms | Beats 96.44% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory
21.54 MB | Beats 34.87%

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/count-servers-that-communicate/description)
