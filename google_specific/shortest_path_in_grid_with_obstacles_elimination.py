from collections import deque, OrderedDict


def get_min_paths_to_end(grid, total_obstacles_that_can_be_surpassed):
    visited = OrderedDict() # using Ordered dict for debugging purpose. Debugger shows the ordering of keys in 'visited'
    possible_dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque()
    steps = 0
    num_rows, num_cols = len(grid), len(grid[0])

    # UNDERSTAND WHY 'K' SHOULD BE TAKEN INTO CONSIDERATION IN THE VISITED
    # IF YOU CONSTRCT THE SOLUTION USING DFS, 'K' WILL BE ONE OF THE PARAMETERS (STATE VARIABLE) IN RECURSION

    start_state = (0, 0, total_obstacles_that_can_be_surpassed)
    q.append((start_state, steps))
    visited[start_state] = True

    while q:
        curr_conf, steps = q.popleft()
        curr_row, curr_col, k = curr_conf

        if (curr_row == num_rows - 1) and (curr_col == num_cols - 1):
            return steps

        for d in possible_dirs:
            new_row, new_col = curr_row + d[0], curr_col + d[1]

            if new_row < 0 or new_row == num_rows or new_col < 0 or new_col == num_cols:
                continue

            new_eliminations = k - grid[new_row][new_col]
            new_state = (new_row, new_col, new_eliminations)

            if new_eliminations >= 0 and new_state not in visited:
                visited[new_state] = True
                q.append((new_state, steps + 1))

    return -1


print(get_min_paths_to_end([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))
print(get_min_paths_to_end([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))
print(get_min_paths_to_end([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 2))
