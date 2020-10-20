class Solution(object):
    def minPathSum(self, grid):
        x = len(grid)
        y = len(grid[0])
        res = [[0 for i in range(y + 1)] for j in range(x + 1)]
        for i in range(x):
            for j in range(y):
                if i == 0:
                    res[i+1][j+1] = res[i+1][j] + grid[i][j]
                elif j == 0:
                    res[i+1][j+1] = res[i][j+1] + grid[i][j]
                else:
                    res[i+1][j+1] = min(res[i+1][j], res[i][j+1]) + grid[i][j]
        return res[x][y]
