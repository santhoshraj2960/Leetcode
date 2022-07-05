# Can I expect only numbers to be in the input?
# If the ques asked to return the actual subarray who prod is max, a suitable follow up qus will be
# 	If I have an input like this [0, -5], there are 2 subarrays whose prod is 0 “[0] and [0, -5]” which one should # I return
# What shoul I return if I get an empty array as input?

"""
eg inputs
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 0, 5]
[0, 4, 5]
[1, 2, 3, -4, 0, 5]
[1, 2, -3, -4, 0, 5]
[2, -2, -3, -5, 0, 5] ---------
[-1, 2, -3, -4, 0, 5]
[-1, -2, -3, 0, -1]
[-1, -2, -3]
"""


def get_max_prod_subarray(arr):
    res = arr[0]  # DO NOT put res = float('-inf'). eg input: [-2]
    max_prod = arr[0]
    min_prod = arr[0]

    for i in range(1, len(arr)):
        curr_num = arr[i]

        temp_max_prod = max_prod  # **EXTREMELY IMPORTANT** should not use max_prod variable in line 36 coz
        # we are modifying it in the next line

        max_prod = max(max_prod * curr_num, min_prod * curr_num, curr_num)  # -2 12 15

        min_prod = min(temp_max_prod * curr_num, min_prod * curr_num, curr_num)  # -4 -3 -60

        res = max(res, max_prod)

    return res

# Try to think of why this solution works
"""
At each step, we do not know if the future element can make the result even bigger
 
"""


print(get_max_prod_subarray([2, -2, -3, -5, 0, 5]))
print(get_max_prod_subarray([1, 2, 3, 4, 5]))
print(get_max_prod_subarray([0, 4, 5]))
print(get_max_prod_subarray([1, 2, 3, -4, 0, 5]))

