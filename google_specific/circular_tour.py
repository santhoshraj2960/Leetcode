# https://practice.geeksforgeeks.org/problems/circular-tour-1587115620/1/?page=1&company[]=Google&sortBy=submissions
"""
Use the following algo
1 - initialize a deque [entire_input + entire_input]
2 - init 2ptrs st and en
3 - init surplus_petrol = 0
4 - surplus_petrol += petrol - dist
5 -  NEED TO SORT THIS OUT

Need to check if the following works
p = 4 5 6 7 8
d = 5 5 7 9 13

j = 0
cq = [0]
ep = -2
j = 1
i = 0
---------------
j = 1
cq = []
i = 1
cq = [1]
j = 2
-------------
j = 2
cq = [1, 2]
j = 3
i = 1
-----------
j = 3
cq = [1, 2, 3]
j = 4 = > 0
i = 1
----------
j = 0
cq = [1, 2, 3, 0]

"""
from collections import deque


def circular_tour(petrol_arr, distance_arr):
    i = 0
    j = 0
    circular_queue = deque()
    excess_petrol = 0

    number_of_start_positions_considered = 0

    while len(circular_queue) <= len(petrol_arr) and number_of_start_positions_considered < len(petrol_arr):
        while excess_petrol < 0 and i < j:
            i = circular_queue.popleft()
            excess_petrol -= (petrol_arr[i] - distance_arr[i])
            i += 1
            i = i % len(petrol_arr)
            number_of_start_positions_considered += 1

        circular_queue.append(j)
        excess_petrol += (petrol_arr[i] - distance_arr[i])
        j += 1
        j = j % len(petrol_arr)

    return i
