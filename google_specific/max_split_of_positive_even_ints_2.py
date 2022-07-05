"""
t = 14
[2,4,6] => curr_sum = 12
[2,4,6,8] => curr_sum = 20 (Don't add 8)
res[-1] = res[-1] + (target - curr_sum) => res[-1] = 6 + (14 - 12) = 8
res = [2,4,8]


t = 28
[2,4,6] => curr_sum = 12
[2,4,6,8] => curr_sum = 20
[2,4,6,8,10] => curr_sum = 30 (Don't add 10)
res[-1] = res[-1] + (target - curr_sum) = 8 + (28 - 20) => 16
res = [2,4,6,16]

"""
from collections import defaultdict


class Solution:
    def maximumEvenSplit(self, final_sum: int) -> List[int]:
        if final_sum % 2 == 1:
            return []

        curr_sum = 0
        res = []

        # Note: "final_sum + 1" || Handles corner case when final_sum is 2 
        # Note: we are incrementing by 2 in the range(st, end, step)
        for i in range(2, final_sum + 1, 2):
            if curr_sum + i <= final_sum:
                curr_sum += i
                res.append(i)
            else:
                break

        res[-1] += final_sum - curr_sum

        return res