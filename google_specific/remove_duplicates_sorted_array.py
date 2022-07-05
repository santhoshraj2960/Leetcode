def return_arr_with_no_duplicates(arr):
    if len(arr) <= 1:
        return len(arr)

    i = 0
    j = 1

    while j < len(arr):
        if arr[i] != arr[j]:
            if j > i + 1:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1

        j += 1

    return i + 1


print(return_arr_with_no_duplicates([2, 3, 4, 5, 6, 6, 6, 7, 8, 9]))
# Now the code works well with the above test case. My next intention is to try and break the code with
# extreme inputs
print(return_arr_with_no_duplicates([2, 2]))
print(return_arr_with_no_duplicates([2]))

print(return_arr_with_no_duplicates([2,3,3,3,3,4,5]))
print(return_arr_with_no_duplicates([2,2,2,2,3,3,3,3,4,5]))
