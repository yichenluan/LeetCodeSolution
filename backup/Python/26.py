class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                nums[i - count] = nums[i]
        return n - count
