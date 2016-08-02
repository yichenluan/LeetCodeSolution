class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for i in range(n)]
        x_start = 0
        y_start = 0
        step = n - 1
        count = 1
        while step > 0:
            for i in range(step):
                res[x_start][y_start] = count
                y_start += 1
                count += 1
            for i in range(step):
                res[x_start][y_start] = count
                x_start += 1
                count += 1
            for i in range(step):
                res[x_start][y_start] = count
                y_start -= 1
                count += 1
            for i in range(step):
                res[x_start][y_start] = count
                x_start -= 1
                count += 1
            x_start += 1
            y_start += 1
            step -= 2
        if count == n * n:
            res[x_start][y_start] = count
        return res
    

if __name__ == '__main__':
    n = 10
    case = Solution()
    res = case.generateMatrix(n)
    for i in res:
        print i
