def rob(house_arr):
    memo = {}

    def steal_max_money_house_robber_helper(index, prev_house_robbed):
        if index == len(house_arr):
            return 0

        if (index, prev_house_robbed) in memo:
            return memo[(index, prev_house_robbed)]

        if prev_house_robbed:
            do_not_steal_house_i = steal_max_money_house_robber_helper(index + 1, False)
            steal_house_i = float('-inf')
        else:
            steal_house_i = house_arr[index] + steal_max_money_house_robber_helper(index + 1, True)
            do_not_steal_house_i = steal_max_money_house_robber_helper(index + 1, False)

        max_profit = max(steal_house_i, do_not_steal_house_i)

        memo[(index, prev_house_robbed)] = max_profit

        return memo[(index, prev_house_robbed)]

    return steal_max_money_house_robber_helper(0, False)


print(rob([1, 2, 3, 1]))
