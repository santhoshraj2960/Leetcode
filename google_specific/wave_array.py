def return_wave_array(arr):
    if len(arr) < 2:
        return arr

    i = 0
    j = 1

    while j < len(arr):
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 2

    return arr

print(return_wave_array([1,2,3,4,5,6]))