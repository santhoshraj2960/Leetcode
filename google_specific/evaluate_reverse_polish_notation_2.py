"""
[2,1,+,3,*]

st = [2, 1] => [3] => [3,3] => [9]
return st[0]

time: O(n)
space: O(n)

    -
13     5  => 13 - 5 = 8  || num on left side (+ or - or / or *) num on right side

Note: the question asks you to truncate towards zero
    - math.floor() will work for +'ve' numberes but FAIL for -'ve' numbers
    - eg: math.floor(2 / 5) = 0 which is truncated to 0
    - eg: math.floor(2 / -5) = -1 which is NOT truncated to 0. Instead it is geting the floor of math.floor(2/-5) = math.floor(-0.4) = -1 => WRONG
        - res = math.ceil(res) if res < 0 else math.floor(res) SOLVES TRUNCATE TO 0
"""
import math


class Solution:
    def evalRPN(self, tokens) -> int:
        st = []

        for ele in tokens:
            # note -11.isdigit() returns False => We try ele[1:].isdigit()
            if ele.isdigit() or ele[1:].isdigit():
                st.append(ele)

            else:
                num_1 = st.pop()
                num_2 = st.pop()

                if ele == '/':
                    res = int(num_2) / int(num_1)
                    res = math.ceil(res) if res < 0 else math.floor(res)
                else:
                    res = eval(num_2 + ele + num_1)

                st.append(str(res))

        return st[0]


