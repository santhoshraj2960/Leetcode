'''
Refer max_split_of_positive_even_ints_2
Greedy appraoch stated here is the most apt solution
https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1783317/JavaPython-3-Greedy-w-brief-explanation-and-analysis.
https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1783191/C%2B%2B-or-Easy-Simulation-or-O(MaximumNumbers)-Time-or-O(1)-Space
'''



# recurse + memo approach || time: O(n^3) || Time Limit Exceeded for 10^4
def maximumEvenSplit(self, finalSum: int) -> List[int]:
    if finalSum % 2 != 0:
        return []

    avail_nums = [i for i in range(2, finalSum + 1) if i % 2 == 0]
    memo = defaultdict(int)

    def helper_recurse(remaining_sum, i):
        nonlocal memo

        if remaining_sum == 0 or i >= len(avail_nums):
            return []

        if (remaining_sum, i) in memo:
            return memo[(remaining_sum, i)]

        if remaining_sum - avail_nums[i] >= 0:
            pick = list(helper_recurse(remaining_sum - avail_nums[i], i + 1))
            skip = list(helper_recurse(remaining_sum, i + 1))

            if len(skip) > len(pick):
                memo[(remaining_sum, i)] = skip
            else:
                pick.append(avail_nums[i])
                memo[(remaining_sum, i)] = pick

            return memo[(remaining_sum, i)]

        else:
            return []

    return helper_recurse(finalSum, 0)

# Backtrack approach || Exponential Time or n! time || Time Limit Exceeded for 10^3
"""
Time compl (Factorial time)
- result could be of atmost length n or n/2 (which is rounded to n)
- We have n slots (_ , _ , _, ..) to fill in and we have n possibilities
- When we fill the first slot with a number n1, n1 cannot be used to fit in any other slots
- Hence for second slot we have (n - 1) possibilities and so on  
"""
def max_even_split(n):
    res = []
    stack = []
    even_nums_upto_n = []
    even_num = 2

    while even_num <= n:
        even_nums_upto_n.append(even_num)
        even_num += 2

    def backtrack(i, curr_sum):
        nonlocal res
        if curr_sum == n:
            if len(stack) > len(res):
                res = list(stack)
            return

        if i == len(even_nums_upto_n):
            return

        if curr_sum + even_nums_upto_n[i] <= n:
            stack.append(even_nums_upto_n[i])
            pick = backtrack(i + 1, curr_sum + even_nums_upto_n[i])
            stack.pop()

        skip = backtrack(i + 1, curr_sum)

    backtrack(0, 0)
    return res


print(max_even_split(12))
