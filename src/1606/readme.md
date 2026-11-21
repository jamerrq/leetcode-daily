# [1606. Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description)

**Level**: <span style="color:red">Hard</span>

You have `k` servers numbered from `0` to `k-1` that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but **cannot handle more than one request at a time**. The requests are assigned to servers according to a specific algorithm:

- The `i^th` (0-indexed) request arrives.
- If all servers are busy, the request is dropped (not handled at all).
- If the `(i % k)^th` server is available, assign the request to that server.
- Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the `i^th` server is busy, try to assign the request to the `(i+1)^th` server, then the `(i+2)^th` server, and so on.

You are given a **strictly increasing** array `arrival` of positive integers, where `arrival[i]` represents the arrival time of the `i^th` request, and another array `load`, where `load[i]` represents the load of the `i^th` request (the time it takes to complete). Your goal is to find the **busiest server(s)**. A server is considered **busiest** if it handled the most number of requests successfully among all the servers.

Return *a list containing the IDs (0-indexed) of the **busiest server(s)***. You may return the IDs in any order.

## Examples

### Example 1:

![](https://assets.leetcode.com/uploads/2020/09/08/load-1.png)

`Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]`

`Output: [1]`

#### Explanation:

- All of the servers start out available.
- The first 3 requests are handled by the first 3 servers in order.
- Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
- Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
- Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

### Example 2:

`Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]`

`Output: [0]`

#### Explanation:

- The first 3 requests are handled by first 3 servers.
- Request 3 comes in. It is handled by server 0 since the server is available.
- Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.

### Example 3:

`Input: k = 3, arrival = [1,2,3], load = [10,12,11]`

`Output: [0,1,2]`

#### Explanation:

Each server handles a single request, so they are all considered the busiest.

## Constraints

- `1 <= k <= 10^5`
- `1 <= arrival.length, load.length <= 10^5`
- `arrival.length == load.length`
- `1 <= arrival[i], load[i] <= 10^9`
- `arrival` is **strictly increasing**.

## My Solution
[index.py](./index.py)

```python
from sortedcontainers import SortedList
import heapq


class Solution:
    def busiestServers(
        self, k: int, arrival: list[int], load: list[int]
    ) -> list[int]:
        idle = SortedList(range(k))  # currently free servers
        busy: list[tuple[int, int]] = []  # min-heap of (finish_time, server_id)
        count = [0] * k
        max_count = 0

        for i, t in enumerate(arrival):
            # free all servers that have finished by time t
            while busy and busy[0][0] <= t:
                _, sid = heapq.heappop(busy)
                idle.add(sid)

            if not idle:
                continue  # all busy → drop request

            # find first free server >= i % k (wrap around if needed)
            preferred = i % k
            idx = idle.bisect_left(preferred)
            sid = idle[0] if idx == len(idle) else idle[idx]

            # assign the request
            idle.remove(sid)
            heapq.heappush(busy, (t + load[i], sid))
            count[sid] += 1
            max_count = max(max_count, count[sid])

        return [i for i in range(k) if count[i] == max_count]
```

## Runtime
631 ms | Beats 15.69%

## Memory
45.92 MB | Beats 61.89% ![clapping_hands](../../lib/clapping_hands.svg)

## Link
[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description)
