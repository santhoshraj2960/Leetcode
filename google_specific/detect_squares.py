"""
Refer second solution here
https://leetcode.com/problems/detect-squares/discuss/1471958/C%2B%2BJavaPython-2-approaches-using-HashMap-with-Picture-Clean-and-Concise
"""

from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.y_dict = defaultdict(list)
        self.points_tups = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.y_dict[point[1]].append(point)  # {10: [[3,10]], 2:[[11,2], [3,2]], }
        self.points_tups[(point[0], point[1])] += 1  # {(3,10): 1, (11,2): 1, (3,2): 1}

    def count(self, point: List[int]) -> int:
        res = 0
        p1 = point  # (x=11,y=10)
        x1, y1 = point

        for x2, y2 in self.y_dict[y1]:  # p2 = [3,10]
            if x2 == x1: continue

            side_len = abs(x1 - x2)  # 8

            x3, y3 = (x1, y1 + side_len)  # (11, 18)
            x4, y4 = (x2, y1 + side_len)

            res += self.points_tups[(x3, y3)] * \
                   self.points_tups[(x4, y4)]

            x3, y3 = (x1, y1 - side_len)  # (11, 2)
            x4, y4 = (x2, y1 - side_len)

            res += self.points_tups[(x3, y3)] * \
                   self.points_tups[(x4, y4)]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
