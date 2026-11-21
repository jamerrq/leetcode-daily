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
