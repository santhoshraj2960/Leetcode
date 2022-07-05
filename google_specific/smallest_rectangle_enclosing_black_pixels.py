"""
We need the following to calc area the smallest rect
- min and max 'x' axis value
- min and max 'y' axis value

then => area = (max x val - min x val + 1) * (max y val - min y val + 1)
Note the IMPORTANCE of "+1" above!
For the example given, max_x = 2 | min_x = 0 | min_y = 1 | max_y = 2
area = (2 - 0 + 1) * (2 - 1 + 1) = 3 * 2 = 6
"""
from collections import deque


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        min_x = max_x = x
        min_y = max_y = y
        q = deque([(x, y)])
        visited = set([(x, y)])

        while q:
            x, y = q.popleft()

            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_x, new_y = x + d[0], y + d[1]

                if -1 < new_x < len(image) and -1 < new_y < len(image[0]) and (new_x, new_y) not in visited and \
                        image[new_x][new_y] == "1":
                    min_x, max_x, min_y, max_y = min(min_x, new_x), max(max_x, new_x), min(min_y, new_y), max(max_y,
                                                                                                              new_y)
                    q.append((new_x, new_y))
                    visited.add((new_x, new_y))

        return (max_x - min_x + 1) * (max_y - min_y + 1)
