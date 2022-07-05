from collections import defaultdict

import heapq


class Solution:
    def swimInWater(self, grid) -> int:
        all_d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        depth_of_start_cell = grid[0][0]
        priority_q = [(depth_of_start_cell, 0, 0)]
        heapq.heapify(priority_q)
        res = float('-inf')
        seen = set()
        num_rows = num_cols = len(grid)

        while priority_q:
            depth_of_curr_cell, curr_r, curr_c = heapq.heappop(priority_q)
            res = max(res, depth_of_curr_cell)

            if curr_r == curr_c == num_rows - 1:
                return max(res, depth_of_curr_cell)

            for d in all_d:
                new_row, new_col = curr_r + d[0], curr_c + d[1]

                if ((-1 < new_row < num_rows) and (-1 < new_col < num_cols)) and (new_row, new_col) not in seen:
                    depth_of_new_cell = grid[new_row][new_col]
                    heapq.heappush(priority_q, (depth_of_new_cell, new_row, new_col))
                    seen.add((new_row, new_col))

        # approach 3: This approach does not work

        # An arbitrary cell can be reached from any of 4 adjacent cells.
        # the parent from which you reached a cell defines the state.
        # For ex. See eg 2 in problem statement.
        # - cell (2,1) that has value 13
        #   - can be reached from path 0,1,2,3,4,5,21,22,23,24,12,13 || In this case, memo[(2,1)] = 17 (this is INCORRECT)
        #   - can be reached from path 0,1,2,3,4,5,16,15,14,13 || In this case, memo[(2,1)] = 13 (this is CORRECT)
        #   - The only diff here is the path we took to reach 13 which determines memo[(2,1)]
        #   - So, memo should be of the form memo[(curr_row, curr_col, parent_row, parent_col)] and in this case, we will have a time compl of O(n * 4) which will give TLE
        #   (Have not implemented this approach because it will get extremely complicated and cannot be successfully done in interviews)
        #   - Follow heaps (or dijikstra) apprach stated in solutions tab

        # Why is this problem different from longest_increasing_path_in_a_matrix? Why can't we use the same approach we used in longest_increasing_path_in_a_matrix?
        #   - As a rule of thumb (what I'm going to state might be worng but I think it makes sense now): When we have to keep track of eles in recursion stack to
        #   avoid infinite loop scenario, it's an undirected graph. The order in which we visit the cells matter. You can go from node a to node b. SImulatenously, you can also
        #   go from node b to node a. Visiting node b (then node a) first might give a diff ans compared to visiting node a first (then node b)
        #   - But in case of longest_increasing_path_in_a_matrix, this is a directed graph. There is a forward edge from node(3) to node(4). But you cannot go from node(4) to node(3)
        #   bacasue it's not a strictly increasing path
        #       - So, we don't have to keep track of nodes in the recursion stack. Because an infinite loop cannot occur

        """
        all_d = [[0,1], [0,-1], [1,0], [-1,0]]
        num_rows = len(grid)
        num_cols = len(grid[0])
        memo = defaultdict(int)
        recursion_stack = set()

        def dfs(row, col):
            nonlocal recursion_stack, memo

            if row == num_rows - 1 and col == num_cols - 1:
                return grid[row][col]

            min_time_needed_from_cell = float('+inf')

            for d in all_d:

                new_row, new_col = row + d[0], col + d[1]

                if (not ((-1 < new_row < num_rows) and (-1 < new_col < num_cols))) or ((new_row, new_col) in recursion_stack):
                    continue


                if (new_row, new_col) in memo:
                    min_time_needed_from_cell = min(min_time_needed_from_cell, memo[(new_row, new_col)])
                else:
                    recursion_stack.add((row, col))
                    min_time_needed_from_cell = min(min_time_needed_from_cell, dfs(new_row, new_col))
                    recursion_stack.remove((row, col))

            memo[(row,col)] = max(min_time_needed_from_cell, grid[row][col])

            return memo[(row,col)]

        recursion_stack.add((0,0))
        res = dfs(0,0)
        a = list(memo.items())
        a.sort()
        print(a)
        return res
        """

        # approach 2: working approach
        """
        time: O(n^2 *k) where n is the num of rows and k is the max val of any cell in the matrix => but if you see one of the constraints (0 <= grid[i][j] < n^2) 
        mentioned in the question, the max val of any cell in the matrix is n^2.
        # So k will be utmost n ^ 2 => time: O(n^2 * n^2) => O(N ^ 4)

        memo = {}
        all_d = [[0,1],[1,0],[0,-1],[-1,0]]
        num_rows = num_cols = len(grid)
        res = float('+inf')
        recursion_stack = set()

        def dfs(i, j, max_val_along_path):
            nonlocal recursion_stack, memo, res

            if i == j == num_rows - 1:
                max_val_along_path = max(max_val_along_path, grid[i][j])
                res = min(res, max_val_along_path)
                return res

            if (i,j,max_val_along_path) in memo:
                return memo[(i,j,max_val_along_path)]


            local_max = float('+inf')

            for d in all_d:
                new_row, new_col = i + d[0], j + d[1]

                if (-1 < new_row < num_rows and -1 < new_col < num_cols) and ((new_row, new_col) not in recursion_stack):
                    recursion_stack.add((new_row, new_col))
                    local_max = min(local_max, dfs(new_row, new_col, max(max_val_along_path, grid[i][j])))
                    recursion_stack.remove((new_row, new_col))

            memo[(i,j,max_val_along_path)] = local_max

            return memo[(i,j,max_val_along_path)]

        return dfs(0,0,0)
        """


# Use the below for debugging purpose (INCORRECT APPROACH)
class Solution:
    def swimInWater(self, grid) -> int:
        all_d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        num_rows = len(grid)
        num_cols = len(grid[0])
        memo = defaultdict(int)
        recursion_stack = []

        def dfs(row, col):
            nonlocal recursion_stack, memo

            if row == num_rows - 1 and col == num_cols - 1:
                return grid[row][col]

            min_time_needed_from_cell = float('+inf')

            if row == 2 and col == 1:
                print('debug')  # debug break point

            for d in all_d:

                new_row, new_col = row + d[0], col + d[1]

                if (not ((-1 < new_row < num_rows) and (-1 < new_col < num_cols))) or (
                        (new_row, new_col) in recursion_stack):
                    continue

                if (new_row, new_col) in memo:
                    min_time_needed_from_cell = min(min_time_needed_from_cell, memo[(new_row, new_col)])
                else:
                    recursion_stack.append((row, col))
                    min_time_needed_from_cell = min(min_time_needed_from_cell, dfs(new_row, new_col))
                    recursion_stack.remove((row, col))

            memo[(row, col)] = max(min_time_needed_from_cell, grid[row][col])

            return memo[(row, col)]

        recursion_stack.append((0, 0))
        res = dfs(0, 0)
        a = list(memo.items())
        a.sort()
        print(a)
        return res

s = Solution()
grid = [[0,2],[1,3]]
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(s.swimInWater(grid))