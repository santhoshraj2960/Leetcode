"""
Below solution is O(n^2) -> TLE
"""
from collections import OrderedDict


class Solution:
    def oddEvenJumps(self, arr) -> int:
        # Using OrderedDict for debugging purpose only
        odd_jumps_from_index_possible = OrderedDict()
        even_jumps_from_index_possible = OrderedDict()

        odd_jumps_from_index_possible[len(arr) - 1] = True
        even_jumps_from_index_possible[len(arr) - 1] = True

        def get_index_to_the_right_for_odd_numbered_jump(i):
            curr_max, max_index = float('+inf'), None

            for j in range(index + 1, len(arr)):
                if arr[i] <= arr[j] and arr[j] < curr_max:
                    curr_max = arr[j]
                    max_index =  j

            return max_index

        def get_index_to_the_right_for_even_numbered_jump(i):
            curr_min, min_index = float('-inf'), None
            for j in range(index + 1, len(arr)):
                if arr[i] >= arr[j] and arr[j] > curr_min:
                    curr_min = arr[j]
                    min_index = j

            return min_index

        for index in range(len(arr) - 2, -1, -1):
            next_jump_index = get_index_to_the_right_for_even_numbered_jump(index)

            even_jumps_from_index_possible[index] = odd_jumps_from_index_possible[next_jump_index] if next_jump_index else False

            next_jump_index = get_index_to_the_right_for_odd_numbered_jump(index)

            odd_jumps_from_index_possible[index] = even_jumps_from_index_possible[next_jump_index] if next_jump_index else False

        """
        odd_jumps_from_index = {4: True, 3: True, 2:False, 1:False, 0: False}
        even_jumps_from_index = {4: True, 3: False, 2:False, 1: False, 0: False}
        """
        res_set = set()

        for index in odd_jumps_from_index_possible: res_set.add(index) if odd_jumps_from_index_possible[index] else res_set
        #for index in even_jumps_from_index_possible: res_set.add(index) if even_jumps_from_index_possible[index] else res_set

        return len(res_set)

s = Solution()
jumps = [10,13,12,14,15]
print(s.oddEvenJumps(jumps))
jumps = [2,3,1,1,4]
print(s.oddEvenJumps(jumps))
jumps = [5,1,3,4,2]
print(s.oddEvenJumps(jumps))
jumps = [1,2,1,4,4]
print(s.oddEvenJumps(jumps))
