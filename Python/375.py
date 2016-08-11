class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        MAX = float('inf')
        # dp array, dp[i][j] represents the min price for guessing number between i and j
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        
        for d in range(1, n):
            for i in range(1, n - d + 1):
                j = i + d
                price = MAX
                for k in range(i, j + 1):
                    price = min(price, 
                                k + max(0 if (k == i) else dp[i][k - 1],
                                        0 if (k == j) else dp[k + 1][j]))
                    
                dp[i][j] = price
        
        return dp[1][n]
