"""
Understand the greedy approach: https://leetcode.com/problems/jump-game-ii/solution/
(The diagram in this page should come to your mind)

N = 11
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3
Explanation:
First jump from 1st element to 2nd  element with value 3. Now, from here we jump to 5th element with value 9,
and from here we will jump to last.
"""


def get_min_jumps_to_reach_end(jumps_arr):
    """

    Returns min num of jumps to reach end from start

    :param jumps_arr: non negative integer array representing jump length from given index
    :return: min num of jumps to reach end
    """

    def minJumps(self, arr, n):
        if len(arr) == 1:
            return 0

        nums = arr
        farthest = 0
        curr_end = 0
        jumps = 0

        for i in range(len(nums)):

            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                curr_end = farthest
                jumps += 1

            if curr_end >= len(nums) - 1:
                break

            if curr_end <= i:
                return -1

        return jumps


print(get_min_jumps_to_reach_end([1, 3, 2]))
print(get_min_jumps_to_reach_end([3, 2, 1]))


print(get_min_jumps_to_reach_end([1, 5, 1, 1, 1, 0, 1, 8]))
print(get_min_jumps_to_reach_end([1, 5, 1, 1, 1, 0, 0, 8]))
print(get_min_jumps_to_reach_end([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(get_min_jumps_to_reach_end([1, 4, 3, 2, 6, 7]))
