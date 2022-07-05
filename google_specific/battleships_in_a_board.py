class Solution:
    def countBattleships(self, board) -> int:
        visited = set()
        num_battleships = 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in visited or board[row][col] == '.':
                    continue

                for d in [[1, 0], [0, 1]]:
                    new_row = row
                    new_col = col
                    while new_row + d[0] < len(board) and new_col + d[1] < len(board[0]) and board[new_row][
                        new_col] == 'X':
                        new_row, new_col = new_row + d[0], new_col + d[1]
                        visited.add((new_row, new_col))

                num_battleships += 1

        return num_battleships
