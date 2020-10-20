class Solution(object):
    def productExceptSelf(self, nums):
        len_nums = len(nums)
        res = [1] * len_nums
        temp = 1
        for i in range(len_nums - 1):
            temp *= nums[i]
            res[i + 1] = temp
        temp = 1
        for i in range(len_nums - 1, 0, -1):
            temp *= nums[i]
            res[i - 1] *= temp
        return res
