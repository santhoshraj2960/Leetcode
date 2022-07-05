"""
# DO not assume that the arrival_time_list and departure_time_list are sorted eg inp: [910, 915, 1000, 800], [920, 950,1010, 1200]
For the above input,you need 3 platforms. If you assume that inputs are sorted and solve_problem, code will output
2 platforms (THIS IS WRONG => see the function "get_min_platforms_inputs_sorted_assumption")

# Do all trains arive and depart on the same day?

# If the arr time of train 1 is same as dep time of train 2 => Do I need seperate platforms?

Input: n = 6

arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}

Output: 3

Explanation:
Minimum 3 platforms are required to safely arrive and depart all trains.
"""

import heapq

# INCORRECT SOLUTION
def get_min_platforms_inputs_sorted_assumption(arr_time_list, dep_time_list):
    max_platforms_needed = 0
    platformes_needed_at_time_i = 0
    departure_time_of_trains_at_platform = [float('+inf')]
    dep_time_list.sort()

    for i, curr_train_arrival_time in enumerate(arr_time_list):

        while departure_time_of_trains_at_platform[0] <= curr_train_arrival_time:

            heapq.heappop(departure_time_of_trains_at_platform)
            platformes_needed_at_time_i -= 1

        heapq.heappush(departure_time_of_trains_at_platform, dep_time_list[i])
        platformes_needed_at_time_i += 1

        max_platforms_needed = max(max_platforms_needed, platformes_needed_at_time_i)

    return max_platforms_needed


# CORRECT SOLUTION time O(n log n) space: O(n)
def get_min_platforms_heaps(arr_time_list, dep_time_list):
    arr_dep_tuples = [(arr_time_list[i], dep_time_list[i]) for i in range(len(arr_time_list))]
    arr_dep_tuples.sort()

    arr_time_list = [tup[0] for tup in arr_dep_tuples]
    dep_time_list = [tup[1] for tup in arr_dep_tuples]

    max_platforms_needed = 0
    platformes_needed_at_time_i = 0
    departure_time_of_trains_at_platform = [float('+inf')]

    for i, curr_train_arrival_time in enumerate(arr_time_list):

        # ******* "<=" is wrong in the below line *****
        # Read the qus CAREFULLY => "same platform can not be used for both departure of a train and arrival of another train"
        while departure_time_of_trains_at_platform[0] < curr_train_arrival_time:
            heapq.heappop(departure_time_of_trains_at_platform)
            platformes_needed_at_time_i -= 1

        heapq.heappush(departure_time_of_trains_at_platform, dep_time_list[i])
        platformes_needed_at_time_i += 1

        max_platforms_needed = max(max_platforms_needed, platformes_needed_at_time_i)

    return max_platforms_needed


# time: O(n) space: O(1)
# 2 ptr solution
# Outer loop loops through departure time.
# At departure_time 'i' how many trains have arrived?
# For each train that arrived AT AND BEFORE (while loop condition => arr_time_list[j] <= dep_time_list[i]) time 'i',
# we need one additional platform

# In the previous approaches the outer loop is based on arrival time. At arrival_time 'i' how many previous trains are
# are still in the station (How many prev trains have their departure_time < arrival_time 'i')
def get_min_platforms(arr_time_list, dep_time_list):
    dep_time_list.sort()
    arr_time_list.sort()

    max_platforms_needed = 0
    platforms_needed_at_time_i = 0

    i = 0
    j = 0

    while i < len(dep_time_list):
        while j < len(arr_time_list) and  arr_time_list[j] <= dep_time_list[i]:
            j += 1
            platforms_needed_at_time_i += 1
            max_platforms_needed = max(max_platforms_needed, platforms_needed_at_time_i)

        platforms_needed_at_time_i -= 1

        i += 1

    return max_platforms_needed

print(get_min_platforms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
print(get_min_platforms([910, 915, 1000, 800], [920, 950,1010, 1200])) #
"""
800   910   915   1000
920   950   1010  1200 
915 920 916
919 921 930

915 916 920
919 921 930
"""

"""
910 900 
920 1200
"""

# Geek for geeks O(n) solution
# Take advantage of the fact that the range of input is fixed
# arr_time and dep_time will ONLY BE BETWEEN [0000, 0001, .. 2359]
def minPlatform(arrival, departure, n):
    # As time range from 0 to 2359 in
    # 24 hour clock, we declare an array
    # for values from 0 to 2360
    platform = [0] * 2361
    requiredPlatform = 1

    for i in range(n):
        # Increment the platforms for arrival
        platform[arrival[i]] += 1

        # Once train departs we decrease the
        # platform count
        platform[departure[i] + 1] -= 1

    # We are running loop till 2361 because
    # maximum time value in a day can be 23:60
    for i in range(1, 2361):
        # Taking cumulative sum of
        # platform give us required
        # number of platform for every minute
        platform[i] = platform[i] + platform[i - 1]
        requiredPlatform = max(requiredPlatform,
                               platform[i])

    return requiredPlatform


# Driver code
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",
      minPlatform(arr, dep, n))

# This code is contributed by PawanJain1
