class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # q = deque()
        pos = (0, 0)
        # q.append_right((pos, (0,1)))
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def go_back():
            # Go back to parent cell using the following commands
            robot.turnRight()  # turn right 90
            robot.turnRight()  # turn one more right 90
            # Now you have turned the robot by 180 degrees
            # Move one step to go back to parent
            robot.move()  # Here we are back to the parent cell

            # Now we need to change the direction to the original direction (since we changed the direction of
            # the robot in the previous 3 lines)
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell, d):
            robot.clean()

            for i in range(4):
                new_dir_ind = (d + i) % 4
                new_cell = (cell[0] + directions[new_dir_ind][0],
                            cell[1] + directions[new_dir_ind][1])

                if new_cell not in visited and robot.move():
                    visited.add(new_cell)
                    backtrack(new_cell, new_dir_ind)
                    go_back()

                robot.turnRight()

        visited.add((0, 0))
        backtrack((0, 0), 0)
