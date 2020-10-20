class Solution(object):
    def findMin(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        left = 0
        right = len_nums - 1
        mid = left + (right - left + 1) / 2
        while nums[mid] >nums[mid - 1]:
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
            mid = left + (right - mid + 1) / 2
        return nums[mid]
