class Solution(object):
    def firstMissingPositive(self, nums):
        l = [0] * (len(nums) + 1)
        for i in nums:
            if i > 0 and i < len(nums) + 1:
                l[i] = 1
        for i in range(1, len(nums) + 1):
            if l[i] == 0:
                return i
        return len(nums) + 1
