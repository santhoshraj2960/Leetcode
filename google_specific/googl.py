def rearrange_around_pivot(arr, st, en):
    pivot = arr[en]
    ptr1 = ptr2 = st

    while ptr2 < en:
        if arr[ptr2] < pivot:
            arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
            ptr1 += 1

        ptr2 += 1

    arr[ptr1], arr[en] = arr[en], arr[ptr1]

    return ptr1


arr = [7, 10, 4, 20, 15]
st = 0
en = len(arr) - 1
k = 4
correctly_placed_element_at_position = -1

while correctly_placed_element_at_position != k - 1:
    correctly_placed_element_at_position = rearrange_around_pivot(arr, st, en)

    if correctly_placed_element_at_position < k:
        st = correctly_placed_element_at_position + 1
    else:
        en = correctly_placed_element_at_position - 1

print(arr[correctly_placed_element_at_position])
