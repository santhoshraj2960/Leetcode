"""
RX XL RX R XL
XR LX XR R LX

"XX XX XL XX XX" => "XX XX LX XX XX
"LX XX XX XX XX"

https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/873004/Easy-to-understand-explanation-with-PICTURE
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False

        pos_of_l_start = [i for i, ch in enumerate(start) if ch == 'L']
        pos_of_l_end = [i for i, ch in enumerate(end) if ch == 'L']

        # print(pos_of_l_start)
        # print(pos_of_l_end)

        pos_of_r_start = [i for i, ch in enumerate(start) if ch == 'R']
        pos_of_r_end = [i for i, ch in enumerate(end) if ch == 'R']

        for i, j in zip(pos_of_l_start, pos_of_l_end):
            if j > i:
                return False

        for i, j in zip(pos_of_r_start, pos_of_r_end):
            if j < i:
                return False

        return True
