import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        m = len(tasks)
        idle = [
            (server_weight, server_id)
            for server_id, server_weight in enumerate(servers)
        ]
        heapq.heapify(idle)
        busy: list[tuple[int, int]] = []  # release time, server id
        ans: list[int] = []
        ts = 0
        task_index = 0
        while task_index < m:
            ts = max(ts, task_index)

            while busy and busy[0][0] <= ts:
                _, server_id = heapq.heappop(busy)
                heapq.heappush(idle, (servers[server_id], server_id))

            if not idle:
                ts = busy[0][0]
                continue

            _, server_id = heapq.heappop(idle)
            ans.append(server_id)

            task = tasks[task_index]
            heapq.heappush(busy, (ts + task, server_id))
            task_index += 1

        return ans
