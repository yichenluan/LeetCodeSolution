class Solution(object):
    def search(self, nums, target):

        def handler(left, right):
            if left == right:
                return nums[left] == target
            mid = (left + right) / 2
            if nums[left] == nums[right]:
                return handler(left, mid) or handler(mid + 1, right)
            if nums[left] < nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target >= nums[left] or target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return handler(left, right)

        n = len(nums)
        left = 0
        right = n - 1
        return handler(left, right)
