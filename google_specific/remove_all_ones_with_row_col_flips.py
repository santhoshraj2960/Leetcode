"""
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1698026/Java-solution-(with-explanation)
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1694045/C%2B%2B-or-followed-hints-or-Explained
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation

eg matrix 1
000
111
flip row 1 

eg matrix 2
101 => 001 => 000
111    011    010

- Try to make row 0 as 0's by col flips. Keep track of flipped cols in a set
- Go to row 1 (Check if all cols of row 1 is 1 and if flip if true) (check if all cols of row 1 is 0 and contnue to next col)
- If the above cond does not hold return False

"""


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def col_flip(col_num):
            nonlocal grid

            for row in range(num_rows):
                grid[row][col_num] = 0 if grid[row][col_num] == 1 else 1

            return

        # Flip all cols in row 0 whose value is 1
        for col in range(num_cols):
            if grid[0][col] == 1: col_flip(col)

        # print(grid)
        # check if subsequent rows are either 1's or 0's
        for row in range(1, num_rows):
            num_zeros = 0
            num_ones = 0
            for col in range(0, num_cols):
                if grid[row][col] == 0:
                    num_zeros += 1
                else:
                    num_ones += 1

            if num_zeros == num_cols or num_ones == num_cols:
                continue
            else:
                return False

        return True
