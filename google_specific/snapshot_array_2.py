class SnapshotArray:

    def __init__(self, length: int):
        """
        [[index_0_snap_arrays], [index_1_snap_arrays]]

        [
        [[0,5], [1,6],... ]
        []
        ]
        """
        self.outer_array = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        inner_array = self.outer_array[index]

        if inner_array[-1][0] == self.snap_id:
            inner_array[-1][1] = val
        else:
            inner_array.append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        inner_array_to_binary_search = self.outer_array[index]

        st = 0
        en = len(inner_array_to_binary_search) - 1

        while st < en:
            mid = math.ceil((st + en) / 2)

            if inner_array_to_binary_search[mid][0] > snap_id:
                en = mid - 1
            else:
                st = mid

        return inner_array_to_binary_search[st][1]
