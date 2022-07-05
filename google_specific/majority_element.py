'''
Ask the interviewer what you should return when there is no majority ele
Ask the interviewer what you should return when the array is empty

Moore's voting is the best approach. Follow that approach if you get this qus in interview
Refer https://leetcode.com/problems/majority-element/solution/ to understand how Moore's voting algo works
'''
from collections import defaultdict

# O(n) time and O(n) space
def return_maority_element(arr):
    elements_dict = defaultdict(int)
    num_of_req_occurances = len(arr) / 2
    '''
    NOTE: num_of_occurances should be GREATER THAN HALF (Not just equal to half)
    len(arr) = 4 => 4/2 = 2 => We need 3 occurances
    len(arr) = 3 => 3/2 = 1.5 => We need 2 occurances
    
    '''

    for ele in arr:
        elements_dict[ele] += 1

        if elements_dict[ele] > num_of_req_occurances:
            return ele

    return -1


print(return_maority_element([1,2,1]))

'''
Using heaps we can solve the problem in 
O(n log n) time and O(1) space using heaps

heapq.heapify(arr)
num_of_popped_eles = 0
prev_ele = flat('-inf')
curr_occurances = 0
max_occuraces = 0
max_occuring_ele = -1

while num_of_popped_eles < len(arr):
    min_ele_from_heap = heapq.heappop()
    
    if min_ele_from_heap != prev_ele:
        if curr_occurances > max_occuraces:
            max_occuraces = curr_occurances
            max_occuring_ele = prev_ele
            
        curr_occurances = 0
        prev_ele = min_ele_from_heap
            
    else:
        curr_occurances += 1
            

if max_occurances > len(arr) / 2:
    return max_occuring_ele
    
else:
    return -1      
            
    
    
###### approach 3 ####
Moore's majority voting algo -> O(n) time and O(1) space
https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/

for curr_ele in arr:
    if curr_ele == prospective_candidate_for_majority:
        count += 1
    
    else:
        count -= 1
    
    if count == 0:
        prospective_candidate_for_majority = curr_ele
        count = 1
    
for curr_ele in arr:
    if prospective_candidate_for_majority == curr_ele:
        num_occurances_of_prospective_candidate_for_majority += 1

if num_occurances_of_prospective_candidate_for_majority > len(arr) / 2:
    return num_occurances_of_prospective_candidate_for_majority
else:
    return -1
'''