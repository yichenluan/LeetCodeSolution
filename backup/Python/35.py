class Solution(object):
    def searchInsert(self, nums, target):
        len_nums = len(nums)
        left = 0
        right = len_nums - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return left
