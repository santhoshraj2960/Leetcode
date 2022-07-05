import math

class SnapshotArray:
    def __init__(self, length: int):
        self.arr = []

        for i in range(length):
            self.arr.append([[0,0]])
        #[
        # [[0,0]],
        # [[0,0]],
        # [[0,5],[1,6],[2,7],
        # [[0,0]],
        # [[0,0]]
        # ]
        # (0 + 2) // 2 = 1 => st = 1
        # (1 + 2) // 2 = 1 => st = 1
        self.curr_snapshot_id = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.curr_snapshot_id:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.curr_snapshot_id, val])

        return

    def snap(self):
        self.curr_snapshot_id += 1
        return self.curr_snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Look at leet_code_backup1.py "Binary Search Block" (first 2 points) to understand how the following binary
        search works, especially why math.cel() is used
        """
        sub_arr = self.arr[index]
        st = 0
        en = len(sub_arr) - 1

        while st < en:
            mid = math.ceil((st + en) / 2)

            if sub_arr[mid][0] == snap_id:
                return sub_arr[mid][1]

            elif sub_arr[mid][0] < snap_id:
                st = mid

            else:
                en = mid - 1

        return sub_arr[st][1]


s = SnapshotArray(5)
s.set(0, 5)
s.snap()
s.set(0, 6)
print(s.get(0,0))
s.snap()
s.set(0, 7)
print(s.get(1,2))
