def get_peak_elem(arr):
    if len(arr) == 1:
        return 0

    def helper(st, en):
        mid_ind = (st + en) // 2
        mid_ele = arr[mid_ind]

        if mid_ind == 0:
            return 0 if arr[0] > arr[1] else 1  # replace this line with return 0 will fail for testcase [1, 2]

        elif mid_ind == len(arr) - 1:
            return len(arr) - 1

        if mid_ele >= arr[mid_ind - 1] and mid_ele >= arr[mid_ind + 1]:
            return mid_ind

        elif mid_ele < arr[mid_ind - 1]:
            return helper(st, mid_ind - 1)

        elif mid_ele < arr[mid_ind + 1]:
            return helper(mid_ind + 1, en)

    # print(helper(0, len(arr) - 1))
    return helper(0, len(arr) - 1)


print(get_peak_elem([1, 2, 2]))
print(get_peak_elem([2, 3]))
print(get_peak_elem([3]))
