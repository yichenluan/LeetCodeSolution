'''
we have the following state equations:
suppose the number of paths to arrive at a point (i, j) is denoted as P[i][j], 
it is easily concluded that P[i][j] = P[i - 1][j] + P[i][j - 1].
'''
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * (n+1)] * (m+1)
        if n == 1 or m == 1:
            return 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j -1] 
        return dp[m][n]


if __name__ == '__main__':
    m,n = 2,2
    case = Solution()
    print case.uniquePaths(m, n)
