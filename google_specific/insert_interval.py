# https://leetcode.com/problems/insert-interval/

"""
[10, 13], ...
[2,5]

[1,2] [3,4],[5,8],[9,11][13,15]
[6,10]
merged_interval = [min(5,6), max(8,10)] => [5,10]
res = [[1,2],[3,4],[5,10]]
if new_interval start is less than first interval start
    append new_interval to start res
    return res

if new_interval start is greater than last interval end
    append new_interval to end res
    return res

else interval somewhere in between
 Find first interval whose end is greater than new_interval start
 This is where we need to insert the new interval


"""


class Solution:
    def insert(self, intervals, new_interval):
        res = []

        if not intervals:
            return [new_interval]

        if intervals[0][0] > new_interval[1]:
            res.append(new_interval)
            res.extend(intervals)
            return res

        if intervals[-1][1] < new_interval[0]:
            res = intervals
            res.append(new_interval)
            return res

        i = 0

        while i < len(intervals):
            if intervals[i][1] >= new_interval[0]:
                break
            else:
                res.append(intervals[i])
                i += 1

        if intervals[i][0] > new_interval[1]:
            res.append(new_interval)
        else:
            merged_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
            res.append(merged_interval)
            i + 1

        while i < len(intervals):
            last_inserted_interval = res[-1]
            if last_inserted_interval[1] >= intervals[i][0]:
                merged_interval = [min(intervals[i][0], last_inserted_interval[0]), max(intervals[i][1], \
                                                                                        last_inserted_interval[1])]
                res.pop()
                res.append(merged_interval)
            else:
                res.append(intervals[i])

            i += 1

        return res