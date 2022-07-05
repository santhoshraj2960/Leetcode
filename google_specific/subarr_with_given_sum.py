"""
Nonneg integers
Continuous sub array that adds to sum s

N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return an array consisting only one element that is -1.
"""


def return_continuous_sub_array_that_adds_to_sum(arr, target):
    """

    :param arr: input array of non neg integers
    :param target: integer target
    :return:
    """
    running_sum = 0
    # {sum: index} running sum at index “-1” (before the start of array) is 0
    running_sum_dict = {0: -1}

    for i, ele in enumerate(arr):
        running_sum += ele
        running_sum_dict[running_sum] = i + 1

        if running_sum - target in running_sum_dict:
            start_ind = running_sum_dict[running_sum - target] + 1
            return [start_ind, i + 1]

    return -1


print(return_continuous_sub_array_that_adds_to_sum([1, 2, 3, 7, 5], 12))
