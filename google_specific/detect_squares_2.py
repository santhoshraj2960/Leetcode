from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.x_coord_dict = defaultdict(set)
        """
        {
        3: set(10, 2),
        11: set(2)
        }
        """
        self.coord_tuples_dict = defaultdict(int)
        """
        (3,10): 1
        (11,2): 1
        (3,2): 1
        """

    def add(self, point) -> None:
        x, y = point[0], point[1]
        self.coord_tuples_dict[(x, y)] += 1
        self.x_coord_dict[x].add(y)

    def count(self, point) -> int:
        x1, y1 = point[0], point[1]
        x2 = x1
        num_of_sq = 0

        for y2 in self.x_coord_dict[x2]:
            """
            example test case that fails if the foll if condition is absent
            ["DetectSquares","add","add","add","add","count"]
            [[],[[3,10]],[[11,10]],[[11,2]],[[3,2]],[[11,10]]]
            Note: [11, 10] is the imaginary point (given as input for "count") but we already have a point at [11,10]. So, sq_side_len = 0 => x3 = 11 => y3 => 10 => x4 = 11  => y4 = 2 => res += 3 || We assumed only 2 points (11, 10) and (11,2) to form 3 squares (This is INCORRECT)
            """
            if y1 == y2: continue  # IF you have a point already located at location of given point
            sq_side_len = abs(y1 - y2)

            x3 = x1 - sq_side_len
            y3 = y1
            x4 = x2 - sq_side_len
            y4 = y2

            num_of_sq += (self.coord_tuples_dict[(x2, y2)] * self.coord_tuples_dict[(x3, y3)] * self.coord_tuples_dict[
                (x4, y4)])

            x3 = x1 + sq_side_len
            y3 = y1
            x4 = x2 + sq_side_len
            y4 = y2

            num_of_sq += (self.coord_tuples_dict[(x2, y2)] * self.coord_tuples_dict[(x3, y3)] * self.coord_tuples_dict[
                (x4, y4)])

        return num_of_sq

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)