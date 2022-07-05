"""
123 (mc = 2 || pc = 1 || st = 1)
    - 123 (1 + 2+ 1+ 2 + 1 = 7)
    - 2:03 (2 + 1 + 2 + 1 + 2 + 1 = 9)
    - 02:03 (more than above)

1 (mc = 2 || pc = 1 || st = 1)
    - 1 (1)
    - 01 (2 + 1 + 2 + 1 = 6)
"""


class Solution:
    def minCostSetTime(self, start_at: int, move_cost: int, push_cost: int, target_seconds: int) -> int:
        op_3 = None

        # eg test case: 150 seconds can be fed into microwave as => 2:30 (or) 1:90 || 1:90 is the case op_3 handles
        if target_seconds % 60 < 40:
            op_3 = str((target_seconds // 60) - 1)
            op_3 += str(60 + target_seconds % 60)

        # -----------------

        op_2 = None

        # eg: testcase: 6008 seconds || 6008 // 60 = 100 minutes || but we cannot input more than 2 digits for minutes in microwave
        # So 6008 seconds can be given as input by manipulating it as per option 3 => 99 minutes and 68 seconds
        if target_seconds // 60 < 100:
            op_2_minutes = str((target_seconds // 60))
            op_2_seconds = str((target_seconds % 60))

            if len(op_2_seconds) == 1: op_2_seconds = '0' + op_2_seconds

            op_2 = op_2_minutes + op_2_seconds

        # -------------------

        # eg: 108 seconds cannot be input into microwave as 108 coz it will be interpretted as 1:08 (68s) and it is wrong
        # Therefore only if the time is < 100, it can be fed as input directly to microwave
        op_1 = str(target_seconds) if len(str(target_seconds)) < 3 else None

        def get_cost(time):
            prev_digit = str(start_at)
            total_time = 0

            for digit in time:
                if digit == prev_digit:
                    total_time += push_cost
                else:
                    total_time += (push_cost + move_cost)

                prev_digit = digit

            return total_time

        op_1_time = get_cost(op_1) if op_1 else float('+inf')

        op_2_time = get_cost(op_2) if op_2 else float('+inf')

        op_3_time = get_cost(op_3) if op_3 else float('+inf')

        return min(op_1_time, op_2_time, op_3_time)
