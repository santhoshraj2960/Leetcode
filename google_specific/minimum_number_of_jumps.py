"""
Need to understand Kadane algorithm (DP + Greedy) as it forms the basics for this problem
Kadane algo finds out what is the max ending at a certain index?
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

https://leetcode.com/problems/jump-game-ii/solution/ (The diagram in this page should come to your mind)

"""

# Can I assume that I can always reach the end?
# Is there a possibility that I should handle where I can't reach the end eg: [3,2,1,0,0]

# [1, 4, 3,2,2,0, 0, 0]

# approach 1 O(n) time O(1) space - Santhosh approach (more intutive)
# Don't try the below approach in interview. It's big and difficult to finish in 20 mins.
# See what happened
#               - https://leetcode.com/submissions/detail/694970411/
#               - https://leetcode.com/submissions/detail/694976260/
# greedy approach mentioned below and in minimum_number_of_jumps_2.py is the one to use in iterviews
# Understand greedy approach better here https://leetcode.com/problems/jump-game-ii/solution/

def get_min_jumps(jumps_arr):
    if len(jumps_arr) == 1:
        return 0

    max_jumps_poss_from_last_location = jumps_arr[0]
    jumps = 0
    i = 1

    max_jump_to_ind_for_next_jump = None

    while i < len(jumps_arr):

        if max_jump_to_ind_for_next_jump:
            max_jumps_poss_from_last_location = max_jump_to_ind_for_next_jump

        max_jump_to_ind_for_next_jump = float('-inf')

        while i <= max_jumps_poss_from_last_location and i < len(jumps_arr):
            jump_to_loc_from_curr_ind = i + jumps_arr[i]
            max_jump_to_ind_for_next_jump = max(
                max_jump_to_ind_for_next_jump,
                jump_to_loc_from_curr_ind
            )
            i += 1

        jumps += 1

        if i >= len(jumps_arr):
            return jumps

        if max_jump_to_ind_for_next_jump < i:
            return -1

    return jumps


print(get_min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(get_min_jumps([1, 4, 3, 2, 6, 7]))
print(get_min_jumps([1, 4, 3, 2, 2, 0, 0, 0]))
print(get_min_jumps([1, 4, 3, 2, 2, 0, 1, 0]))
print(get_min_jumps([1]))
print(get_min_jumps([1, 0]))
print(get_min_jumps([0, 0]))


# approach 2 O(n) time and O(1) space - Geekforgeeks
def get_min_number_of_jumps(jumps_arr):
    steps = jumps_arr[0]
    max_reach = jumps_arr[0]
    jumps = 0

    for i in range(1, len(jumps_arr)):
        if max_reach >= len(jumps_arr) - 1:
            return jumps + 1

        reach_from_current_ind = jumps_arr[i] + i
        max_reach = max(max_reach, reach_from_current_ind)
        steps -= 1

        if steps == 0:

            jumps += 1
            steps = max_reach - i

            if i > max_reach:
                return -1


# print(get_min_number_of_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))