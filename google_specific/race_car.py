from collections import OrderedDict, deque

"""

s 1.   2.   4.   -1.  -2   -1   -2
0 -> 1 -> 3 -> 7 -> 7 -> 6 -> 6 -> 5 
   A.   A.   A.   R.   A   R    A

"""
"""
q = [(1, -1, 2), (-1, -2, 2), (0, 1, 2)]
visited = [(0,1,0), (1, 2, 1), (-1, -2, 2), (0, 1, 2)]
"""


def get_shortest_dist_to_target(target):
    q = deque()
    visited_dict = OrderedDict()

    initial_state = (0, 1, 0)
    q.append(initial_state)
    visited_dict[initial_state] = True

    while q:
        prev_pos, speed, steps = q.popleft()  # (3, 4, 2)

        if prev_pos == target:
            return steps

        # ---- option 1 ----- accelerate -----
        pos = prev_pos + speed  # -1
        new_state_option_1 = (pos, speed * 2, steps + 1)  #

        # ---- option 2 ----- rev -----
        if speed > 0:
            option_2_speed = -1
        else:
            option_2_speed = 1

        new_state_option_2 = (prev_pos, option_2_speed, steps + 1)  #

        if new_state_option_1 not in visited_dict:
            if 2 * abs(target - prev_pos) < abs(target - pos) or pos < 0:
                # At the current pos, you are farther away from the target than you were in your prev pos
                pass
            else:
                q.append(new_state_option_1)
                visited_dict[new_state_option_1] = True

        if new_state_option_2 not in visited_dict:
            q.append(new_state_option_2)
            visited_dict[new_state_option_1] = True


print(get_shortest_dist_to_target(10000))
