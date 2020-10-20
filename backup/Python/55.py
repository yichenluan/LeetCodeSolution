class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if dp[j] == True and nums[j] >= i - j:
                    dp[i] = True
                    break
        return dp[n-1]


class Solution(object):
    def canJump(self, nums):
        n = len(nums) - 1
        jump = n
        for i in xrange(n-1, -1, -1):
            if i+nums[i] >= jump:
                jump = i
        return jump == 0 or i+nums[i] >=n
