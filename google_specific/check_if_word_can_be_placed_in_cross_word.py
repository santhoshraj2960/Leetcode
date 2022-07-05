"""
starting at a random cell k, we have 2 poss
    - place the word in the right (or)
    - place the word in the bottom

Refer https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/discuss/1486285/Python-3-working-with-strings
for a shorter solution (key point in solution in this link is "for B in board,zip(*board)" )
"""


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        grid = board
        num_rows = len(board)
        num_cols = len(board[0])

        def check_if_word_can_be_placed_starting_at_cell_to_right(row, col):
            can_be_placed = True
            i = 0

            while i < len(word):
                if (col < num_cols) and (board[row][col] == word[i] or board[row][col] == ' '):
                    i += 1
                    col += 1
                else:
                    can_be_placed = False
                    break

            return can_be_placed

        def check_if_word_can_be_placed_starting_at_cell_to_bottom(row, col):
            can_be_placed = True
            i = 0

            while i < len(word):
                if (row < num_rows) and (board[row][col] == word[i] or board[row][col] == ' '):
                    i += 1
                    row += 1
                else:
                    can_be_placed = False
                    break

            return can_be_placed

        for word in [word, word[::-1]]:
            for row in range(num_rows):
                for col in range(num_cols):
                    if grid[row][col] == '#':
                        continue
                    """
                    The ordering of if condition below MAKES OR BREAKS the deal (for TLE).
                    If you rearrange the if condition such that 
                    check_if_word_can_be_placed_starting_at_cell_to_right(row, col)
                    comes first, you will get a TLE

                    It does not affect the time complexity (as it takes same amount of time in the worst case)
                    worst case:[['.', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#', '.', '#', ]
                                Same row as above for 100 times
                                ]
                                word: 'pen'
                    """
                    if (col == 0 or grid[row][col - 1] == '#') and \
                            (col + len(word) == num_cols or \
                             (col + len(word) < num_cols and grid[row][col + len(word)] == "#")
                            ) and \
                            check_if_word_can_be_placed_starting_at_cell_to_right(row, col):
                        return True

                    if (row == 0 or grid[row - 1][col] == '#') and \
                            (row + len(word) == num_rows or \
                             (row + len(word) < num_rows and grid[row + len(word)][col] == "#")
                            ) and \
                            check_if_word_can_be_placed_starting_at_cell_to_bottom(row, col):
                        return True

        # NOTICE how adding the outer for loop "for word in [word, word[::-1]]:" helped us comment the repetitive lines of code below
        """
        word = word[::-1]

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '#':
                    continue

                if (col == 0 or grid[row][col - 1] == '#') and \
                    (col + len(word) == num_cols or \
                        (col + len(word) < num_cols and grid[row][col + len(word)] == "#")
                    ) and \
                    check_if_word_can_be_placed_starting_at_cell_to_right(row, col):
                        return True

                if (row == 0 or grid[row -1][col] == '#') and \
                    (row + len(word) == num_rows or \
                     (row + len(word) < num_rows and grid[row + len(word)][col] == "#")
                    ) and \
                    check_if_word_can_be_placed_starting_at_cell_to_bottom(row, col):
                        return True

        """

