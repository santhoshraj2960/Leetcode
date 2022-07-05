from collections import defaultdict


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        """
        point_to_end_map = {
        1: 4,
        2: 4,
        3: 4,
        }
        """
        point_to_end_map = defaultdict(int)
        res = []

        for p in paint:
            area_painted = 0
            st = p[0]
            en = p[1]

            while st < en:
                if st in point_to_end_map:
                    st = point_to_end_map[st]
                else:
                    point_to_end_map[st] = en
                    st += 1
                    area_painted += 1

            res.append(area_painted)

        return res


"""
time O(N) N is the max number in the number_line in the input. We will not paint (or) visit any point more than once
space O(N)
"""

amountPainted([[1, 4], [5, 8], [4, 9]])

"""
def get_painted_area_each_day(all_paint_intervals):
boundary_dict = {}
portion_painted_each_day = []

      for paint_interval in all_paint_intervals:
		interval_start = paint_interval[0]
		interval_end = paint_interval[1]
		portion_painted_today = 0
		
		while interval_start < interval_end:
			if interval_start in boundary_dict:
				interval_start = boundary_dict[interval_start]
				boundary_dict[interval_start] = max(interval_end, 
boundary_dict[interval_start]
			else:
				boundary_dict[interval_start] = interval_end
				portion_painted_today += 1
interval_start += 1

		portion_painted_each_day.append(portion_painted_today)
	
	return portion_painted_each_day

‘’’
time: O(N) -> Where N is the length of the wall
space: O(N) -> Where N is the length of the wall

​​[[1,4],[5,8],[4,7],[4,11]]
portion_painted_each_day = [3,3,1]

paint_interval = [4,11]
interval_start = 4
interval_end = 11

boundary_dict[1] = 4
boundary_dict[2] = 4
boundary_dict[3] = 4
boundary_dict[5] = 8
boundary_dict[6] = 8
boundary_dict[7] = 8
boundary_dict[4] = 7

portion_painted_today = 1

‘’’

"""