class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [1] * len(nums)
        prev_index = [-1] * len(nums)
        max_len = 0
        max_index = -1

        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = prev_index[max_index]
        return res
