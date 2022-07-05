"""
helper(0, 0, 0)
	num_of_poss = 0
    - helper(1, 0, 0)
        - helper(2, 0, 0) -> return 1
        - helper(2, 1, 0) -> return 1
        - helper(2, 0, 1) -> return 1

    - helper(1, 1, 0)
        - helper(2, 1, 0) -> return 1
        - helper(2, 1, 1) -> return 1

    - helper(1, 0, 1)
        - helper(2, 0, 0) -> return 1
        - helper(2, 1, 0) -> return 1
        - helper(2, 0, 1) -> return 1

    num_of_poss = 8
"""
"""
If you have time look at the dp arroach below
https://leetcode.com/problems/student-attendance-record-ii/discuss/101643/Share-my-O(n)-C%2B%2B-DP-solution-with-thinking-process-and-explanation
"""

def get_num_of_combinations_for_award(n):
    memo = {}

    def helper(ith_day, num_absents, num_of_consecutive_late_days):
        nonlocal memo
        if ith_day == n:
            return 1

        if (ith_day, num_absents, num_of_consecutive_late_days) in memo:
            #print('memo hit')
            return memo[(ith_day, num_absents, num_of_consecutive_late_days)]

        num_of_poss = 0

        if num_absents == 1:
            if num_of_consecutive_late_days == 2:
                num_of_poss += helper(ith_day + 1, num_absents, 0)
            else:
                # num_of_consecutive_late_days is 0 or 1
                num_of_poss += helper(ith_day + 1, num_absents, 0)
                num_of_poss += helper(ith_day + 1, num_absents,
                                      num_of_consecutive_late_days + 1)

        else:
            # num_of_absent is 0
            if num_of_consecutive_late_days == 2:
                num_of_poss += helper(ith_day + 1, num_absents, 0)
                num_of_poss += helper(ith_day + 1, num_absents + 1, 0)
            else:
                # num_of_consecutive_late_days is 0 or 1
                num_of_poss += helper(ith_day + 1, num_absents, 0)
                num_of_poss += helper(ith_day + 1, num_absents + 1, 0)

                num_of_poss += helper(ith_day + 1, num_absents,
                                      num_of_consecutive_late_days + 1)

        memo[(ith_day, num_absents, num_of_consecutive_late_days)] = num_of_poss
        return memo[(ith_day, num_absents, num_of_consecutive_late_days)]

    return helper(0, 0, 0)

# time O(n) recursive fun ith day has 3 params -> ith_day has n possibilites, num_absents has 2 and
#           num_of_consecutive_late_days has 3 possibilites
# space O(n) height of recursion stack (or tree)

print(get_num_of_combinations_for_award(1))
print(get_num_of_combinations_for_award(2))
print(get_num_of_combinations_for_award(10101))
