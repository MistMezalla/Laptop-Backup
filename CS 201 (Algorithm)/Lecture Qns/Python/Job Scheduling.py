# Single Server
class Solution1:
    def minimize_time_in_system(self, jobs):
        jobs.sort(key=lambda x: x[1])

        total_time = 0
        current_time = 0

        for job, processing_time in jobs:
            current_time += processing_time
            total_time += current_time

        return total_time


jobs = [('j1', 3), ('j2', 1), ('j3', 2), ('j4', 5)]
sol1 = Solution1()
print(sol1.minimize_time_in_system(jobs))

#On multiple servers

import heapq
class Solution2:
    def minimize_time_on_m_servers(self, jobs, m):
        jobs.sort(key=lambda x: x[1])
        servers = [0] * m
        total_time = 0

        for job, processing_time in jobs:
            earliest_server = heapq.heappop(servers)
            total_time += earliest_server + processing_time
            heapq.heappush(servers, earliest_server + processing_time)

        return total_time

jobs = [('j1', 3), ('j2', 1), ('j3', 2), ('j4', 5)]
sol2 = Solution2()
print(sol2.minimize_time_on_m_servers(jobs, 2))

