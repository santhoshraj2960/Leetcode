"""
This is a problem where we need
- sorted key value pairs (in order to get min price and max price in LESS than O(n) time)
- Retrieve the a key in O(1) time (in order to update the price of a time in the past)
- Insert a new key and still maintain the sorted order of keys

- Ordereddict() solves the first 2 usecases mentioned above but fails to satisfy 3rd usecase
- Heaps helps to insert a new item into it and maintain sorted order but we cannot retrieve and update a key in O(1) or O(log n) time. Updating a key in heap (in worst case) takes O(n log n) time

So, we need a datastructure that maintains the ordering (or sorted condition) as well as retreive and update in O(1) time

Sorted dictionary inserts a new item in O(log n) time. Updates, get_min_key and get_max_key are O(1) time

Refer
- https://leetcode.com/problems/stock-price-fluctuation/discuss/1513345/Map-and-Multiset
- https://leetcode.com/problems/stock-price-fluctuation/discuss/1513413/JavaC%2B%2BPython-Strightforward-Solutions
"""
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.price_to_time_map = SortedDict()
        self.time_to_price_map = SortedDict()
        # By default sorteddict() values are not of any datatype (eg.set(), list(), etc.) We have to manually assing it
        # see this line below """self.price_to_time_map[price] = set([timestamp])"""

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_price_map:
            old_price = self.time_to_price_map[timestamp]
            self.price_to_time_map[old_price].remove(timestamp)

            if len(self.price_to_time_map[old_price]) == 0: self.price_to_time_map.pop(old_price)

        if price in self.price_to_time_map: self.price_to_time_map[price].add(timestamp)
        else: self.price_to_time_map[price] = set([timestamp])

        self.time_to_price_map[timestamp] = price

    def current(self) -> int:
        return self.time_to_price_map.peekitem(-1)[1]


    def maximum(self) -> int:
        return self.price_to_time_map.peekitem(-1)[0]


    def minimum(self) -> int:
        return self.price_to_time_map.peekitem(0)[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()