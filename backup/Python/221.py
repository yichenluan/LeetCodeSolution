class Solution(object):
    def maximalSquare(self, matrix):
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxArea = 0
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                maxArea = max(maxArea, dp[i][j])
        return maxArea * maxArea
