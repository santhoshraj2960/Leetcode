import math


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        st = 0
        en = len(nums) - 1

        while st < en:
            mid = (st + en) // 2

            if nums[mid] < target:
                st = mid + 1
            else:  # nums[mid] >= target
                en = mid

        left_most = st if nums[st] == target else -1

        st = 0
        en = len(nums) - 1

        while st < en:
            mid = math.ceil((st + en) / 2)

            if nums[mid] > target:
                en = mid - 1
            else:  # nums[mid] <= target
                st = mid

        right_most = st if nums[st] == target else -1

        return [left_most, right_most]
