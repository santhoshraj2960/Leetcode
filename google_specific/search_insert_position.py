class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        st = 0
        en = len(nums) - 1

        while st < en:
            mid = math.ceil((st + en) / 2)

            if nums[mid] > target:
                en = mid - 1
            else:
                st = mid

        return st + 1 if nums[st] < target else st
