from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.num_of_cols = None
        self.num_of_rows = None
        self.visited_dict = defaultdict(tuple)
        self.mat = None

    # This func will be called exactly (or utmost) once for every cell
    # Everything we do inside this fun is a constant
    # This is similar to DFS and we visit a node only once
    def mark_all_connected_lands_of_island_as_visited(self, row_num, col_num):
        # You have to set visited to TRUE here and NOT INSIDE the for loop to prevent infinite loop
        # eg: mat = [[0, 1],
        #	         [1,0]]

        self.visited_dict[(row_num, col_num)] = True

        possible_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #                       [1, 1], [1, -1], [-1, 1], [-1, -1]]
        # If diagonal elements are to be considered as connected, uncomment the above line

        # The following for loop is constant O(1)
        # It will loop exactly 4 times (or 8 times if diagonal elements are to be considered as connected)
        for direction in possible_directions:
            new_row = row_num + direction[0]
            new_col = col_num + direction[1]

            if new_row < 0 or new_row >= self.num_of_rows or \
                    new_col < 0 or new_col >= self.num_of_cols or \
                    (new_row, new_col) in self.visited_dict or \
                    self.mat[new_row][new_col] == 0:
                continue

            else:
                self.mark_all_connected_lands_of_island_as_visited(new_row, new_col)

        return True

    def get_num_of_islands(self, mat):
        self.mat = mat
        self.num_of_rows = len(mat)
        self.num_of_cols = len(mat[0])
        num_islands = 0

        for row_num in range(self.num_of_rows): # O(n)

            for col_num in range(self.num_of_cols): # O(m)

                if (row_num, col_num) in self.visited_dict or mat[row_num][col_num] == 0:
                    continue

                else:
                    self.mark_all_connected_lands_of_island_as_visited(row_num, col_num)
                    num_islands += 1

        return num_islands

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.get_num_of_islands(grid)


i = Solution()
print(i.numIslands([[0,1],[1,0],[1,1],[1,0]]))
print(i.numIslands([[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]))

# time O(n * m) where n and m represent the number of rows and cols
# space O(n * m)