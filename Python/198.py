class Solution(object):
    def rob(self, nums):
        len_nums = len(nums)
        res = [0 for i in range(len_nums)]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len_nums -1, -1, -1):
            if i == len_nums - 1:
                res[i] = nums[i]
            elif i == len_nums - 2:
                res[i] = max(nums[i], nums[i+1])
            else:
                res[i] = max(nums[i] + res[i+2], res[i+1])
        return res[0]
