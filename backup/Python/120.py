class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        res = list()

        def dfs(curr, index, nums):
            if curr == n - 1:
                res.append(sum(nums))
                return
            dfs(curr + 1, index, nums + [triangle[curr+1][index]])
            dfs(curr + 1, index + 1, nums + [triangle[curr+1][index+1]])

        dfs(0, 0, [triangle[0][0]])
        return min(res)


class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

class Solution(object):
    # O(n*n/2) space, top-down 
    def minimumTotal1(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
