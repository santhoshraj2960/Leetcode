"""
prod_of_arr = 120
prod_until_ind = [3, 3, 6, 30, 120]
get_prod(2) => return prod_of_arr / prod_until_ind[len(prod_until_ind) - k - 1] => 120 / prod_until_ind[2] => 120/6 = 20
index_of_last_zero = 1

prod_of_arr = 120
prod_until_ind = [3, 3, 6, 30, 120]
index_of_last_zero = 1

get_prod(2)
- if 1 and 1 >= (5 - 2)
- else: return 120 / self.prod_until_index[5 - 2 - 1] => 120/6 => 20

"""


class ProductOfNumbers:

    def __init__(self):
        # NOTE: understand why we initialized prod_of_arr to 1 and prod_until_index to [1]
        # When you add only 1 element add(7) and then getProd(1) => you should return the element that you added (i.e. 7)

        # If you dont initialize prod_of_arr = None and prod_until_index = [] || after you add 7 || prod_of_arr = 7 and
        # prod_until_index = [7]
        # Now when you call getProd(1) with the above config || the else part in the getProd will become
        # return self.prod_of_arr // self.prod_until_index[1 - 1 - 1] => 7 // self.prod_until_index[-1] => 7 // 7 = 1 (THIS IS WRONG)

        # Similar to running_sums_dict where the sum of numbers until index 0 is 0
        # Similarly, the prod of numbers until index 0 is 1
        self.prod_of_arr = 1
        self.prod_until_index = [1]
        self.index_of_last_zero = None

    def add(self, num: int) -> None:
        if num == 0:
            self.index_of_last_zero = len(self.prod_until_index)

            self.prod_until_index.append(self.prod_until_index[-1])

        else:
            self.prod_until_index.append(self.prod_until_index[-1] * num)

        self.prod_of_arr = self.prod_until_index[-1]

    def getProduct(self, k: int) -> int:
        if self.index_of_last_zero != None and self.index_of_last_zero >= len(self.prod_until_index) - k:
            return 0

        else:
            return self.prod_of_arr // self.prod_until_index[len(self.prod_until_index) - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)