class Solution(object):
    def longestIncreasingPath(self, matrix):
        res = 1
        if not matrix:
            return 0
        x_len = len(matrix)
        y_len = len(matrix[0])
        dp = [[0] * y_len for i in range(x_len)]
        for x in range(x_len):
            for y in range(y_len):
                res = max(res, self.dfs(matrix, dp, x, y))
        return res

    def dfs(self, matrix, dp, x, y):
        if dp[x][y]:
            return dp[x][y]
        else:
            x_len = len(matrix)
            y_len = len(matrix[0])
            res1 = res2 = res3 = res4 = 0
            if y > 0 and matrix[x][y-1] > matrix[x][y]:
                res1 = 1 + self.dfs(matrix, dp, x, y-1)
            if x > 0 and matrix[x-1][y] > matrix[x][y]:
                res2 = 1 + self.dfs(matrix, dp, x-1, y)
            if y < y_len - 1 and matrix[x][y+1] > matrix[x][y]:
                res3 = 1 + self.dfs(matrix, dp, x, y+1)
            if x < x_len - 1 and matrix[x+1][y] > matrix[x][y]:
                res4 = 1 + self.dfs(matrix, dp, x+1, y)
            dp[x][y] =  max(res1, res2, res3, res4, 1)
            return dp[x][y]


if __name__ == '__main__':
    # nums = [
        # [3, 4, 5],
        # [3, 2, 6],
        # [2, 2, 7]
        # ]
    nums = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

    case = Solution()
    print case.longestIncreasingPath(nums)
