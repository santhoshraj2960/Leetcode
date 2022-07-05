def max_profit_stocks(stock_price_arr):
    if len(stock_price_arr) < 2:
        return 0

    i = 1
    profits_arr = []

    while i < len(stock_price_arr):
        # stock price is depreciating -> going towards valley
        while i < len(stock_price_arr) and stock_price_arr[i] <= stock_price_arr[i - 1]:
            i += 1

        if i == len(stock_price_arr):
            break

        j = i  # 5

        # stock price is appreciating -> going towards peak
        while j < len(stock_price_arr) and stock_price_arr[j] > stock_price_arr[j - 1]:
            j += 1

        if stock_price_arr[i - 1] < stock_price_arr[j - 1]:
            profits_arr.append([stock_price_arr[i - 1], stock_price_arr[j - 1]])

        i = j + 1  # 5

    return profits_arr


print(max_profit_stocks([100,180,260,310,40,535,695]))
print(max_profit_stocks([100,180,260,310,40,535,20, 695]))
print(max_profit_stocks([100,50,180,260,310,40,535,20, 695]))
print(max_profit_stocks([4,2,2,2,4]))
print(max_profit_stocks([4,2,2,2,2]))
print(max_profit_stocks([4,6,2,2,2]))