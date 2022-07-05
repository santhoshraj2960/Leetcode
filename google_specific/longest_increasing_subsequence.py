def lengthOfLIS(nums) -> int:
    memo = {}

    def lis_helper(i, prev_num_ind):
        if i == len(nums):
            return 0

        if (i, prev_num_ind) in memo:
            return memo[(i, prev_num_ind)]

        if (prev_num_ind is None) or (nums[i] > nums[prev_num_ind]):
            pick_num = 1 + lis_helper(i + 1, i)
            skip_num = lis_helper(i + 1, prev_num_ind)
        else:
            pick_num = float('-inf')
            skip_num = lis_helper(i + 1, prev_num_ind)

        memo[(i, prev_num_ind)] = max(pick_num, skip_num)

        return memo[(i, prev_num_ind)]

    return lis_helper(0, None)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
