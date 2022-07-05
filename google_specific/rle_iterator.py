"""
[3, 8, 0, 9, 2, 5] => [3,8,2,5] =>[[3,8], [2,5]
itr = 0

next(2) => [1, 8, 0, 9, 2, 5]
itr = 0
"""


class RLEIterator:

    def __init__(self, encoding: [int]):
        self.encoded_arr = [[encoding[i], encoding[i + 1]] for i in range(0, len(encoding), 2) if encoding[i] > 0]
        self.itr = 0

    def next(self, n: int) -> int:
        while n > 0 and self.itr < len(self.encoded_arr):
            if self.encoded_arr[self.itr][0] >= n:
                self.encoded_arr[self.itr][0] -= n
                return self.encoded_arr[self.itr][1]
            else:
                n -= self.encoded_arr[self.itr][0]
                self.itr += 1

        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)