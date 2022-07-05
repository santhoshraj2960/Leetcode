# Will the input array have duplicates?
# Can I expect atleast 1 triplet to have a zero sum in the input?
# What should I return if there are no triplets that sum up to zero?
# Can I expect only numbers in the input?
# Should I return the triplet (in other words, the 3 numbers that make up zero sum) or should I return the indices
# of the numbers that make up zero sum?
# If there are 2 or more triplets that sum to zero? Which one should I return

# space O(n)
# time O(n log n)
# In python
# - "sort()" uses timsort -> sorts the list in place. Return True indicating that the list is sorted
# - "sorted()" uses timsort -> creates another list and sorts the elements and return the sorted list
# timsort has a worst case time complexity of O(n log n) and worst case space complexity of O(n). Best case
# timsort space complexity is O(1)
# [4,4,-8]


def check_if_any_triplet_sums_to_zero(arr):
    """
    Checks  if any triplet sums up to zero in array.

    :param arr: array of numbers

    :returns: 1 if any triplet sums up to zero in array.
    :returns: 0 if any triplet sums up to zero in array.
    """
    if len(arr) < 3:
        return 0

    arr.sort()

    for i in range(0, len(arr)):
        elem_at_i = arr[i]

        j = i + 1
        k = len(arr) - 1

        while j < k:
            elem_at_j = arr[j]
            elem_at_k = arr[k]

            sum_of_i_j_k = elem_at_i + elem_at_j + elem_at_k

            if sum_of_i_j_k == 0:
                print(elem_at_i, elem_at_j, elem_at_k)
                return 1

            if sum_of_i_j_k < 0:
                j += 1
            else:
                k -= 1

    return 0



print(check_if_any_triplet_sums_to_zero([60, -65, 5, -21, 8, 93]))
print(check_if_any_triplet_sums_to_zero([4, -16, 43, 4, 7, -36, 18]))
print(check_if_any_triplet_sums_to_zero([97, -27, 2, -34, 61, -39]))