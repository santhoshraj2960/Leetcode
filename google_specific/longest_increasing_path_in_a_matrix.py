from collections import defaultdict

"""
{
(0,0): 1
(0,1): 1
(1,0): 2
}
"""
# SEE swim_in_rising_water to understand how this problem is diff from that. (Directed vs Undirected graph withing matrix)
# time: O(m * n) space: O(m *n)
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        all_d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        visited_dict = defaultdict(int)

        def dfs(row, col):
            nonlocal visited_dict

            max_incr_path_from_cell = 1

            for d in all_d:
                new_row, new_col = row + d[0], col + d[1]

                if not ((-1 < new_row < num_rows) and (-1 < new_col < num_cols)):
                    continue

                if matrix[new_row][new_col] > matrix[row][col]:
                    if (new_row, new_col) in visited_dict:
                        max_incr_path_from_cell = max(max_incr_path_from_cell, 1 + visited_dict[(new_row, new_col)])
                    else:
                        max_incr_path_from_cell = max(max_incr_path_from_cell, 1 + dfs(new_row, new_col))

            visited_dict[(row, col)] = max_incr_path_from_cell
            return visited_dict[(row, col)]

        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) not in visited_dict:
                    dfs(row, col)

        return max(visited_dict.values())

