'''
Can I expect the input array to have just positive numbers?
Or should I expect -ve numbers and alphabets? If yes, how should I handle them? Ignore them
'''

# DP approach

def trap_water_2(arr):
    left_boundary_wall = [-1] * len(arr)
    right_boundary_wall = [-1] * len(arr)

    for i, ele in enumerate(arr):
        if i == 0:
            left_boundary_wall[i] = ele
            continue

        left_boundary_wall[i] = max(ele, left_boundary_wall[i - 1])

    arr.reverse()

    for i, ele in enumerate(arr):
        if i == 0:
            right_boundary_wall[i] = ele
            continue

        right_boundary_wall[i] = max(ele, right_boundary_wall[i - 1])

    right_boundary_wall.reverse()
    arr.reverse()
    trapped_water = 0

    for i in range(len(arr)):
        trapped_water += min(left_boundary_wall[i], right_boundary_wall[i]) - arr[i]

    return trapped_water

# Very hard to explain the following approach on a call.
# Always think of a relatively easier solution (better compared to naive or even naive) and ask the interviewer if
# they are ok with you implementing the easier approach.
# First implement the easier approach and then orally explain the sophisticated approach. Interviewer may not even
# ask you to code it

# stack approach
def trap_water(arr):
    stack = []

    if not arr:
        return 0

    water_stored = 0

    for i, curr_ht in enumerate(arr):

        while stack and arr[stack[-1]] <= curr_ht:
            popped_wall = stack.pop()  # 1
            popped_wall_ht = arr[popped_wall]  # 0

            if not stack:
                break

            left_wall_ht = arr[stack[-1]]  # 3
            height_of_rectangle_boundary = min(left_wall_ht, curr_ht)  # 2
            width = i - stack[-1] - 1  # 2- 0 - 1 = 1
            corrected_height = height_of_rectangle_boundary - popped_wall_ht  # 2 - 0 = 2

            water_stored += corrected_height * width  # 2 * 1 = 2

        stack.append(i)

    '''
    We don't need the following while loop.
    eg input [5,4,0,3]
    At the end of above for loop
    water_stored will hold the value 3
    stack will hold the following values [5,4,3]. We won't be able to store any additional water
    So, the final answer is just 3
    The following while loop does not add any logic
    
    while stack:
        popped_wall = stack.pop()
        popped_wall_ht = arr[popped_wall]

        if not stack:
            break

        if popped_wall_ht <= arr[stack[-1]]: # input that will hit this condition [8, 8, 2, 4, 5, 5, 1]
            continue

        left_wall_ht = arr[stack[-1]]
        height_of_rectangle_boundary = min(left_wall_ht, curr_ht)
        width = i - stack[-1] - 1
        corrected_height = height_of_rectangle_boundary - popped_wall_ht

        water_stored += corrected_height * width
        '''

    return water_stored


print(trap_water([8,8,2,4,5,5,1]))
print(trap_water([3,0,2,0,1,0,2,0,4]))
print(trap_water([3, 0, 2, 0, 1, 0, 2, 4, 0, 3]))
