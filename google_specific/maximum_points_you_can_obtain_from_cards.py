"""
[1,2,3...5,6,1]
[1,2,100,...5,6,1]
[1,2,100,...99,6,1]
[1,2,100,...1,1,99]
[1,99,100,...1,1,1000]
GREEDY wont work

recurse(l, r)
- op_1 = score[l] + recurse(l + 1, r)
- op_2 = score[r] + recurse(l, r - 1)

return max(op_1, op_2)
"""


class Solution:
    def maxScore(self, card_points: [int], k: int) -> int:
        # Approach 1: Sliding window + continuos subarray sum
        # This is a modification of sliding window approach, instead of calculating the max sum of the elements present inside the window,
        # we want to calculate the max sum of the nums outside the window.
        # Look at the solutions tab video to get a better understanding
        start = k - 1
        end = len(card_points) - 1

        max_points = curr_subset_sum = sum(card_points[0:k])

        while start > -1:
            curr_subset_sum -= card_points[start]
            curr_subset_sum += card_points[end]
            max_points = max(max_points, curr_subset_sum)
            start -= 1
            end -= 1

        return max_points

        """
        approach 1 - recursion + memo => time and space: O(k ^ 2)

        memo = {}

        def recurse_max_points(left, right):
            if left + (len(card_points) - right - 1) == k:
                return 0

            if (left, right) in memo: return memo[left, right]

            pick_left = card_points[left] + recurse_max_points(left + 1, right)
            pick_right = card_points[right] + recurse_max_points(left, right - 1)

            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]


        return recurse_max_points(0, len(card_points) - 1)
        """