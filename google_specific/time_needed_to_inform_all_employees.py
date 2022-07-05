"""
{
-1: [(2, 1)]
 2: [(0,0), (1,0), (3,0)]
}
"""

from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, head_id: int, managers_list, inform_time_list) -> int:
        manager_subordinates_map = defaultdict(list)
        max_time_needed = 0

        for employee, manager in enumerate(managers_list):
            manager_subordinates_map[manager].append((employee, inform_time_list[employee]))

        def dfs(manager, inform_time_so_far):
            nonlocal max_time_needed

            if manager not in manager_subordinates_map:
                max_time_needed = max(max_time_needed, inform_time_so_far)
                return

            for subordinate, subordinate_inform_time in manager_subordinates_map[manager]:
                dfs(subordinate, inform_time_so_far + subordinate_inform_time)

        dfs(-1, 0)

        return max_time_needed
