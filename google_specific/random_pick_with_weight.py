import random


class Solution:

    def __init__(self, w):
        self.arr = [w[0]]

        for i in range(1, len(w)):
            self.arr.append(self.arr[i-1] + w[i])

        self.total_sum = sum(w) # also equal to self.arr[-1]

    def pickIndex(self) -> int:
        # following line returns a random float num between 0 and self.total_sum
        target = random.uniform(0, self.total_sum)
        st = 0
        en = len(self.arr) - 1

        while st < en:
            mid = (st + en) // 2
            mid_ele = self.arr[mid]

            if mid_ele < target:
                st = mid + 1
            else:
                en = mid

        return st


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
