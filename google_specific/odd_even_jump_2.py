"""
odd_jumps_possible_set = set(indices from which odd jumps can reach end)
even_jumps_possible_set = set(indices from which event jumps can reach end)

odd_jumps -> Find the smallest poss value (on the right) that is greater than curr_ele
even_jumps -> Find the greatest poss value (on the right) that is lesser than curr_ele
eg: [5,1,3,4,2]
sorted_arr = [(1,1), (2,4), (3,2), (4,3), (5,0)]

stack = []
for a, i in sorted([a, i] for i, a in enumerate(A)):
    while stack and stack[-1] < i:
        next_higher[stack.pop()] = i # index of the smallest number (that is greater than curr number) on the right
    stack.append(i)

stack = [1] || next_higher = [None, None, None, None, None]
stack = [4] || next_higher = [4, N, N, N, N]
stack = [4,2] || next_higher = [4, N, N, N, N]
stack = [4,3] || next_higher = [4, N, 3, N, N]
stack = [4,3,0] || next_higher = [4, N, 3, N, N]

solution referred from https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-using-Map-or-Stack
"""


class Solution:
    def oddEvenJumps(self, arr: [int]) -> int:

        def get_next_higher_or_next_lower(sorted_arr):
            next_higher_or_lower = [None] * len(sorted_arr)
            stack = []
            for ele, ind in sorted_arr:
                while stack and stack[-1] < ind:
                    next_higher_or_lower[stack.pop()] = ind
                stack.append(ind)

            return next_higher_or_lower

        sorted_arr = sorted([(ele, ind) for ind, ele in enumerate(arr)])
        next_higher = get_next_higher_or_next_lower(
            sorted_arr)  # index of the smallest number (that is GREATER than curr number) on the right -> odd jump

        sorted_arr = sorted([(ele, ind) for ind, ele in enumerate(arr)], key=lambda x: -x[0])
        next_lower = get_next_higher_or_next_lower(
            sorted_arr)  # index of the larget number (that is SMALLER than curr number) on the right -> even jump

        higher_jump_poss_indices, lower_jump_poss_indices = [False] * len(arr), [False] * len(arr)
        higher_jump_poss_indices[-1] = lower_jump_poss_indices[-1] = True

        for i in range(len(arr) - 2, -1, -1):
            if next_lower[i] and higher_jump_poss_indices[next_lower[i]]: lower_jump_poss_indices[i] = True

            if next_higher[i] and lower_jump_poss_indices[next_higher[i]]: higher_jump_poss_indices[i] = True

        return sum(higher_jump_poss_indices)


"""
time: O(n log n)
space: O(n)
"""