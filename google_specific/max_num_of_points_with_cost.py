# https://leetcode.com/problems/maximum-number-of-points-with-cost/

def pick_max_vals_from_matrix(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    memo = {}

    def pick_max_vals_from_matrix_helper(row, prev_col):
        if row == num_rows:
            return 0

        if (row, prev_col) in memo:
            print('memo hit')
            return memo[(row, prev_col)]

        local_max_at_curr_row = float('-inf')

        for col in range(num_cols):
            if row == 0:
                max_val_by_picking_this_col = grid[row][col] + pick_max_vals_from_matrix_helper(row + 1, col)
            else:
                max_val_by_picking_this_col = grid[row][col] + pick_max_vals_from_matrix_helper(row + 1, col) - abs(col - prev_col)

            local_max_at_curr_row = max(local_max_at_curr_row, max_val_by_picking_this_col)

        memo[(row, prev_col)] = local_max_at_curr_row
        return memo[(row, prev_col)]

    return pick_max_vals_from_matrix_helper(0, None)


print(pick_max_vals_from_matrix([[1,2,3],[1,5,1],[3,1,1]]))
print(pick_max_vals_from_matrix([[1,5],[2,3],[4,2]]))

# Time O(n * m) n is the num of rows and m is the num of cols => The recursive func takes 2 parameters (row and col)
# We do not compute the same row and same col more than once (because of memo).
# space O(n * m) memo dict will have atmost n * m keys