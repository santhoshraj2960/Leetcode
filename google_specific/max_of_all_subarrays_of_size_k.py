"""

"""

# INCORRECT SOLUTION
def get_max_elem_in_subarrays_of_size_k(arr, k):
    res = []
    index_of_max_elem_in_window = 0  # 2

    for i in range(1, k):
        curr_ele = arr[i]

        if curr_ele >= arr[index_of_max_elem_in_window]:
            index_of_max_elem_in_window = i

    res.append(arr[index_of_max_elem_in_window])  # 3 3 4 5 5 5
    # index_of_max_elem_in_window = 5
    window_end_ind = k  # 8

    while window_end_ind < len(arr):  # 8 < 9
        if window_end_ind - index_of_max_elem_in_window == k:  # 8 - 5 == 3

            curr_window_start = index_of_max_elem_in_window + 1
            index_of_max_elem_in_window = curr_window_start

            while curr_window_start <= window_end_ind:
                if arr[curr_window_start] >= arr[index_of_max_elem_in_window]:
                    index_of_max_elem_in_window = curr_window_start

                curr_window_start += 1

        if arr[window_end_ind] >= arr[index_of_max_elem_in_window]:  # 3 > 5
            index_of_max_elem_in_window = window_end_ind  # 5

        res.append(arr[index_of_max_elem_in_window])

        window_end_ind += 1

    return res


print(get_max_elem_in_subarrays_of_size_k([1, 2, 3, 1, 4, 5, 2, 4, 3, 6], 3))