'''Burst Balloons

dp[i][j] = max(dp[i][j], dp[i][x] + nums[i-1]*nums[x]*nums[j+1] + dp[x][j]
'''
class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for ballons_num in range(1, len(nums) -1):
            for left in range(0, len(nums) - ballons_num - 1):
                right = left + ballons_num + 1
                for x in range(left + 1, right):
                    dp[left][right] = max(
                            dp[left][right],
                            dp[left][x] + nums[left] * nums[x] * nums[right] + dp[x][right]
                        )
        return dp[0][-1]
