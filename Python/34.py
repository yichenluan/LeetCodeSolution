class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        left = None
        right = None
        while l <= r:
            mid = (l + r) / 2
            if target == nums[mid]:
                if mid == 0 or nums[mid-1] < target:
                    left = mid
                    break
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) / 2
            if target == nums[mid]:
                if mid == n-1 or nums[mid+1] > target:
                    right = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if left is None:
            return [-1, -1]
        return [left, right]


if __name__ == '__main__':
    nums = [2, 2]
    target = 2
    case = Solution()
    print case.searchRange(nums, target)
