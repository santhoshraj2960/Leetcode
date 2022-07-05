"""
Valley and Peak approach
https://dev.to/bebopvinh/leetcode-122-the-valleys-and-peaks-approach-5j9 (look at the second approach discussed.
Try to understand the diagram to know why this approach works)

[100, 180, 260, 310, 40, 535, 695]

{100, 180, 310, 260, 40, 535, 695}

{100, 180, 310, 260, 270, 40, 535, 695}
"""

# ------------------------------------------------------------------------------------------------------------------
'''
Best approach - Peak and Valley approach 
https://dev.to/bebopvinh/leetcode-122-the-valleys-and-peaks-approach-5j9 (look at the second approach discussed.
Try to understand the diagram to know why this approach works)

time - O(n)
space O(1)

This approach can also be modified and used when the problem statement says, you can buy and sell only once
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
def max_profit(prices)
    i, max = 0, 0
    valley = prices[0]
    peak = prices[0]
    last = len(prices) - 1

    while i < last
        while (i < last and prices[i] >= prices[i + 1])
            i+= 1

        valley = prices[i]
        valley_ind = i

        while (i < last and prices[i] <= prices[i + 1])
            i += 1

        peak = prices[i]
        peak_ind = i

        res.append([valley_ind, peak_ind])

        # Uncomment the following line if you want to calculate the max profit
        # max_profit += peak - valley

    return res

------------------------------------------------------------------------------------------------------------------

arr = [1000, 100, 180, 260, 310, 40, 535, 695]
#arr = [4,2,2,2,4]
#arr = [4,2,2,2,2]
#arr = [4,6,2,2,2]
memo = [-1] * len(arr)

# get_max_profit calculates the max profit you can get by trading. It does not return the indices of the days
# you have to buy and sell - which is asked in the actual question
# get_stocks_buy_sell_price return the indices of the days you have to buy and sell to get max profit

# get_max_profit is O(n ^ 2) time and O(n) space
# Worst case, we call get_max_profit for every index
# get_max_profit has a for loop which loops over every index greater than curr_ind

def get_max_profit(curr_ind):
    if curr_ind == len(arr):
        return 0

    if memo[curr_ind] != -1:
        return memo[curr_ind]

    current_day_stock_price = arr[curr_ind]
    max_profit_at_curr_ind = 0

    # The following is the case 1: I buy the stock on day: curr_ind
    for i in range(curr_ind + 1, len(arr)):
        stock_price_on_day_i = arr[i]

        if stock_price_on_day_i > current_day_stock_price:
            profit_by_selling_on_day_i = stock_price_on_day_i - current_day_stock_price + \
                                         get_max_profit(i + 1)

            if profit_by_selling_on_day_i > max_profit_at_curr_ind:
                max_profit_at_curr_ind = profit_by_selling_on_day_i

    # The following is case 2: I don't buy the stock on day: curr_ind
    profit_by_not_buying_at_current_ind = get_max_profit(curr_ind + 1)

    max_profit_at_curr_ind = max(profit_by_not_buying_at_current_ind, max_profit_at_curr_ind)
    memo[curr_ind] = max_profit_at_curr_ind

    return memo[curr_ind]

print(get_max_profit(0))


# The following is O(n) time and O(n) space - efficient

def get_stocks_buy_sell_price(arr):
    res = []
    buy_price_ind = 0

    for i in range(1, len(arr)):
        current_day_stock_price = arr[i]
        prev_day_stock_price = arr[i-1]

        if current_day_stock_price < prev_day_stock_price:
            # sell the stock yesterday and buy at today’s price
            if arr[buy_price_ind] < prev_day_stock_price:
                res.append([buy_price_ind, i-1])

            buy_price_ind = i

    last_day_ind = len(arr) - 1
    last_day_stock_price = arr[last_day_ind]

    if last_day_stock_price > arr[buy_price_ind]:
        res.append([buy_price_ind, last_day_ind])

    return res


print(get_stocks_buy_sell_price([100, 180, 260, 310, 40, 535, 695]))
print(get_stocks_buy_sell_price([4,2,2,2,4]))
print(get_stocks_buy_sell_price([4,2,2,2,2]))
print(get_stocks_buy_sell_price([4,6,2,2,2]))
