class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
