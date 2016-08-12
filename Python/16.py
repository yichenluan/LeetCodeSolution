class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = float('inf')
        n = len(nums)
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    return tmp
                if abs(tmp - target) < abs(res - target):
                    res = tmp
        return res
