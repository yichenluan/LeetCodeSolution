class Solution(object):
    def numTrees(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            res_i = 0
            for j in range(1, i + 1):
                res_i = res_i + (dp[j - 1] * dp[i - j])
            dp[i] = res_i
        return dp[n]


if __name__ == '__main__':
    test = Solution()
    n = 3
    print test.numTrees(n)
