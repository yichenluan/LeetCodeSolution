class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for curr in range(1, target + 1):
            for num in nums:
                if num > curr:
                    continue
                dp[curr] += dp[curr - num]
            pass
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    case = Solution()
    print case.combinationSum4(nums, target)
