'''
https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation
'''
"""
how do I know that diff bet 23:59 and 00:00 is 1
[0, 1, ...60,...120, ..720, ...1380, 1439, 1440]
23 * 60 = 1380

eg:1 (Don't assume the times are sorted)
["23:59", "00:00"] =>sort =>["00:00", "23:59"]
["00:00", "23:59"]
times.appedn(times[0] + 1440)
[0, 1439, 1440]
"""

class Solution:
    def findMinDifference(self, timePoints) -> int:
        minutes_list = []

        for time in timePoints:
            minutes = int(time[:2]) * 60 + int(time[-2:])
            minutes_list.append(minutes)

        minutes_list.sort()
        minutes_list.append(minutes_list[0] + (24 * 60))

        minutes_list_without_first_ele = minutes_list[1:]
        res = float('+inf')

        for t1, t2 in zip(minutes_list, minutes_list_without_first_ele):
            res = min(res, t2 - t1)

        return res
