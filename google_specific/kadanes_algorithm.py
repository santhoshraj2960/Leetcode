"""
How and Why does it work?
https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

Kadane algorithm - DP
Kadane algo finds out what is the max ending at a certain index?


arr = [2,1,-3,4,-1,2,1,-5,4]
max_sum_ending_at_ind=
[2,
max(2+1, 1) = 3
max(3 + -3, -3) = 0
max(0 + 4, 4) = 4
max(4 + -1, -1) = 3
max(3 + 2, 2) = 5
max(5 +1, 1) = 6
max(6 + -5, -5) = 1
max(1 + 4, 4) = 5

"""


def get_max_subarray(arr):
    max_sum_ending_at_ind = [float('-inf')] * len(arr)
    max_sum_ending_at_ind[0] = arr[0]

    for i in range(1, len(arr)):
        max_sum_ending_at_ind[i] = max(max_sum_ending_at_ind[i - 1] + arr[i], arr[i])

    return max(max_sum_ending_at_ind)


print(get_max_subarray([2,1,-3,4,-1,2,1,-5,4]))