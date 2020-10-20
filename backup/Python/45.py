class Solution(object):
    def jump(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in xrange(n-2, -1, -1):
            maxJump = nums[i]
            if i + maxJump >= n - 1:
                dp[i] = 1
            else:
                minJump = float('inf')
                for jumpLength in xrange(maxJump, 0, -1):
                    minJump = min(minJump, 1 + dp[i+jumpLength])
                    if minJump == 2:
                        break
                dp[i] = minJump
        return dp[0]


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step
