"""
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
NOTE: NOT SMALLER (which means [1,5,5,4] has a peak element '5')

Following corner cases give better idea about the problem.


If input array is sorted in strictly increasing order, the last element is always a peak element.
For example, 50 is peak element in {10, 20, 30, 40, 50}.

If the input array is sorted in strictly decreasing order, the first element is always a peak element.
100 is the peak element in {100, 80, 60, 50, 20}.

If all elements of input array are same, every element is a peak element.

***** It is clear from the above examples that there is ALWAYS a peak element in the input array. ******


What should I return if there are multiple peak elements in input?
"""

# time O(n) space O(1)
def return_peak_element(arr):
    if len(arr) == 1:
        return arr[0]

    if not arr:  # ask the interviewer what you should return when the array is empty
        return -1

    # what should I return if there are multiple peak elements?
    for i, ele in enumerate(arr):
        if i == 0:
            if ele >= arr[1]:
                return i  # NOTE: you should return the INDEX (i) of the peak element (NOT THE ELEMENT (ele))
            else:
                continue

        if i == len(arr) - 1:  # NOTE: when working with indices -> len(arr) MINUS 1 will give you last index
            if ele >= arr[-2]:
                return i
            else:
                continue

        if ele >= arr[i - 1] and ele >= arr[i - 2]:  # NOTE: NOT SMALLER
            return i


print(return_peak_element([2, 3]))

'''
We can solve this in O(log n) time using binary search (or divide and conquer) approach
https://practice.geeksforgeeks.org/problems/peak-element/1/?page=1&company[]=Google&sortBy=submissions (editorial tab)

The idea is based on the technique of Binary Search to check if the middle element is the peak element or not. 
If the middle element is not the peak element, then check if the element on the right side is greater than the middle 
element then there is always a peak element on the right side. If the element on the left side is greater than the 
middle element then there is always a peak element on the left side. Form a recursion and the peak element can be 
found in log n time.

eg:
7 8 5 4 5 5 3
middle elem is 4 and the elements 5 on the left and 5 on the right are both greater than the middle element. Hence
acording to the theory explained above, there should be a peak element on both (left and right) side of 4. The peak
elem in the left half is 8 and the right half is 5

def binary_search(st, en):
    mid = st + en // 2
    
    if mid == 0:
        if arr[mid] >= arr[mid + 1]:
            return arr[mid]
    
    if mid == len(arr) - 1:
        if arr[mid] >= arr[mid - 1]:
            return arr[mid]
            
    if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
        return mid
    
    elif arr[mid - 1] > arr[mid]:
        return binary_search(st, mid - 1)
        
    else:
        return binary_search(mid + 1, en)  
'''