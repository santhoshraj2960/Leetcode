from collections import defaultdict


class Solution:
    # time: O(n ^ 2)
    def minAreaRect(self, points) -> int:
        min_area = float('+inf')
        points_set = set()

        for point in points:
            points_set.add((point[0], point[1]))

        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1:]):
                # Finidng diagonally opposite points (x1,y1) and (x2,y2)
                # Since we have diagonal points, there is only possibility for the other 2 points

                if x1 == x2 or y1 == y2: continue  # these 2 points cannot form a diagonal of a rect

                # x1, y1: (3,1)
                # x2, y2: (4,3)

                x3, y3 = x1, y2
                x4, y4 = x2, y1

                if (x3, y3) in points_set and (x4, y4) in points_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)

        return min_area if min_area != float('+inf') else 0


    # approach 2
    # The following is complicated approach and will be difficult to explain in an interview
    """
    x_d = {
    '1': set([1, 3])
    '3': set([1, 3])
    '2': set([2])
    }

    y_d = {
    '1': set([1, 3]),
    '3': set([1, 3]),
    '2': set([2,2])
    }

    points_set = set([1,1],[1,3],[3,1],[3,3],[2,2])

    x1 = 1
        - y1 = 1 -> (x1, y1)(1,1)
        - y2 = 3 -> (x2, y2)(1,3)

            y1 = 1
                - x3 = 1 (1,1) ( same point as x1, y1 -> not poss)
                - x3 = 3 -> (x3, y3) (3,1) (connects edge with x1, y1)
                - Only one option to connect edge with (x2, y2) i.e. (x4, y4) => (3, 3)

    """
    def minAreaRect_2(self, points) -> int:
        min_area = float('+inf')
        points_set = set()
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)

        for point in points:
            points_set.add((point[0], point[1]))
            x_dict[point[0]].append(point[1])
            y_dict[point[1]].append(point[0])

        for x1 in x_dict:
            for i, y1 in enumerate(x_dict[x1]):
                for j, y2 in enumerate(x_dict[x1][i + 1:]):
                    # (x1,y1): (1,1)
                    # (x2,y2): (1,3)
                    y3 = y1  # y3 = (_, 1)
                    for x3 in y_dict[y1]:
                        # (1,1) || (3,1) => (x3, y3)
                        if x3 == x1: continue

                        if (x3, y2) in points_set:
                            # (3, 3)
                            # this is rect
                            area = (abs(x3 - x1) * abs(y2 - y1))
                            min_area = min(area, min_area)

        return min_area

points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
#points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
s = Solution()
print(s.minAreaRect(points))