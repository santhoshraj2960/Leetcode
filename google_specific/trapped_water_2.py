# time O(n) space O(1)
def get_trapped_rain_water_two_ptr(walls_arr):
    """
    returns the water trapped in between walls in walls_arr

    :param walls_arr: non-negative integer array
    :return: an integer representing the amount of water trapped in between walls in input array
    """

    water_stored = 0  # 6 + 7 + 7 + 7
    tallest_left_wall_ind = 0
    tallest_right_wall_ind = len(walls_arr) - 1
    l = 0
    r = len(walls_arr) - 1

    # [....7, 8...]
    # [....7, 5, 8...]
    while l <= r:
        if walls_arr[tallest_left_wall_ind] <= walls_arr[tallest_right_wall_ind]:

            if walls_arr[l] > walls_arr[tallest_left_wall_ind]:
                tallest_left_wall_ind = l
            else:
                water_stored += (walls_arr[tallest_left_wall_ind] - walls_arr[l])

            l += 1

        else:

            if walls_arr[r] > walls_arr[tallest_right_wall_ind]:
                tallest_right_wall_ind = r
            else:
                water_stored += (walls_arr[tallest_right_wall_ind] - walls_arr[r])

            r -= 1

    return water_stored


# time O(n) space O(n)
def get_trapped_rain_water_dp(walls_arr):
    """
    returns the water trapped in between walls in walls_arr

    :param walls_arr: non-negative integer array
    :return: an integer representing the amount of water trapped in between walls in input array
    """
    # [3, 3, 3, 3, 3, 4]
    tallest_wall_left = []

    # [4, 4, 4, 4, 4, 4]
    tallest_wall_right = []

    tallest_wall_left.append(walls_arr[0])
    tallest_wall_right.append(walls_arr[len(walls_arr) - 1])
    water_stored = 0

    # i = 1
    for i in range(1, len(walls_arr)):
        tallest_wall_left.append(max(walls_arr[i], tallest_wall_left[-1]))

    for i in range(len(walls_arr) - 1, -1, -1):
        tallest_wall_right.append(max(walls_arr[i], tallest_wall_right[-1]))

    tallest_wall_right.reverse()

    for ind, wall in enumerate(walls_arr):
        boundary_of_rect = min(tallest_wall_left[ind], tallest_wall_right[ind])
        boundary_minus_curr_wall_ht = boundary_of_rect - wall
        water_stored += boundary_minus_curr_wall_ht

    return water_stored


print(get_trapped_rain_water_two_ptr([3, 0, 0, 2, 0, 4]))
print(get_trapped_rain_water_dp([3, 0, 0, 2, 0, 4]))

print(get_trapped_rain_water_two_ptr([3, 0, 0, 2, 5, 4]))
print(get_trapped_rain_water_dp([3, 0, 0, 2, 5, 4]))

print(get_trapped_rain_water_two_ptr([3]))
print(get_trapped_rain_water_dp([3]))

print(get_trapped_rain_water_two_ptr([3, 2]))
print(get_trapped_rain_water_dp([3, 2]))

print(get_trapped_rain_water_two_ptr([3, 2, 3]))
print(get_trapped_rain_water_dp([3, 2, 3]))

print(get_trapped_rain_water_two_ptr([1,0,2,1,1,3]))
print(get_trapped_rain_water_dp([1,0,2,1,1,3]))

print(get_trapped_rain_water_two_ptr([2,1,0,3,2]))
print(get_trapped_rain_water_dp([2,1,0,3,2]))