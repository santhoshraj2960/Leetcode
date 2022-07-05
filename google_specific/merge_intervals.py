# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals):
        intervals = [(i[0], i[1]) for i in intervals]
        intervals.sort()
        res = [intervals[0]]
        i = 1

        while i < len(intervals):
            last_inserted_interval = res[-1]

            if last_inserted_interval[1] >= intervals[i][0]:
                merged_interval = [last_inserted_interval[0], max(last_inserted_interval[1], intervals[i][1])]
                res.pop()
                res.append(merged_interval)
            else:
                res.append(intervals[i])

            i += 1

        return res