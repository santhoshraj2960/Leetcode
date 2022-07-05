"""
2 things to note in the solution
 - Use of tuple
 - Use of else in "for" loop || else corresponding to a for loop executes when the loop completes successfully (i.e. without hitting any 'break' statements)
    -- https://book.pythontips.com/en/latest/for_-_else.html#else-clause

Solution referred from
- https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/discuss/1797403/Python-3-or-DFS-Adjacency-List-or-Explanation
"""
from collections import defaultdict


class Solution:
    def buildWall(self, height: int, width: int, bricks: [int]) -> int:
        curr_config = []
        all_configs = []

        def get_all_configs_for_row_i(rem_width):
            nonlocal all_configs
            if rem_width == 0:
                all_configs.append(tuple(curr_config))
                return

            for brick_size in bricks:
                if brick_size > rem_width:
                    continue

                curr_config.append(brick_size)
                get_all_configs_for_row_i(rem_width - brick_size)
                curr_config.pop()

        get_all_configs_for_row_i(width)
        possible_neighboring_configs_for_config = defaultdict(list)
        # print(all_configs)

        for config in all_configs:
            brick_endings_1 = []
            for brick in config[:-1]:
                if not brick_endings_1:
                    brick_endings_1.append(brick)
                else:
                    brick_endings_1.append(brick_endings_1[-1] + brick)

            # NOTE: the below line will throw an error "brick_endings_1 is not defined"
            # brick_endings_1 = set([config[i] if i == 0 else brick_endings_1[i-1] + config[i] for i in range(len(config))][:-1])

            for neighboring_config in all_configs:
                brick_endings_2 = []
                for brick in neighboring_config[:-1]:
                    if not brick_endings_2:
                        brick_endings_2.append(brick)
                    else:
                        brick_endings_2.append(brick_endings_2[-1] + brick)

                # NOTE: the use of else statement for a "for" loop || else will get executed if the break doesn't execute
                for brick_ending in brick_endings_2:
                    if brick_ending in brick_endings_1: break
                else:
                    possible_neighboring_configs_for_config[config].append(neighboring_config)

        # print(possible_neighboring_configs_for_config)

        ans, mod = 0, int(1e9 + 7)

        # Following cache statement is asking python to use inbuilt memo
        @cache
        def dfs(combo, h):
            nonlocal ans, possible_neighboring_configs_for_config, height
            if height == h: return 1
            return sum(dfs(nei, h + 1) for nei in possible_neighboring_configs_for_config[combo])

        for combo in all_configs:
            ans += dfs(combo, 1) % mod

        return ans % mod
