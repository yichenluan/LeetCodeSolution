class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row,col,m,n,visited,grid):
            visited[row][col] = 1
            if row-1 >= 0 and grid[row-1][col] == '1' and visited[row-1][col] == 0:
                dfs(row-1,col,m,n,visited,grid)
            if row+1 <= m-1 and grid[row+1][col] == '1' and visited[row+1][col] == 0:
                dfs(row+1,col,m,n,visited,grid)
            if col-1 >= 0 and grid[row][col-1] == '1' and visited[row][col-1] == 0:
                dfs(row,col-1,m,n,visited,grid)
            if col+1 <= n-1 and grid[row][col+1] == '1' and visited[row][col+1] == 0:
                dfs(row,col+1,m,n,visited,grid)
            return 
        if len(grid) == 0:  return 0
        else:
            m,n = len(grid),len(grid[0])
            visited,result = [[0]*n for _ in xrange(m)],0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1' and visited[i][j] == 0:
                        dfs(i,j,m,n,visited,grid)
                        result += 1
            return result
