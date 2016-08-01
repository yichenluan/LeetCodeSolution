class Solution(object):
    def permute(self, nums):
        res = [[nums[0]]]
        if len(nums) == 1:
            return res
        for num in nums[1:]:
            temp = list()
            for i in range(len(res[0]) + 1):
                temp += [per[:i] + [num] + per[i:] for per in res]
            res = temp
        return res
