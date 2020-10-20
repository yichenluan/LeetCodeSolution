class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]
