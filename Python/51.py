class Solution(object):
    def solveNQueens(self, n):
        def handler(position, row):
            if row == n:
                res.append(position[:])
                return
            for i in range(len(position)):
                position[row] = i
                if self.isOK(row, i, position):
                    handler(position, row+1)
                # position[row] = 0 
        res = list()
        handler([0 for _ in range(n)], 0)
        return self.formatRes(res)

    def formatRes(self, res):
        format_res = [['.'*index + 'Q' + '.'*(len(position)-index-1) for index in position] for position in res]
        return format_res



    def isOK(self, row, col, position):
        for i in range(row):
            curr_row = i
            curr_col = position[i]
            if curr_col == col:
                return False
            if abs(curr_col - col) == abs(curr_row - row):
                return False
        return True


if __name__ == '__main__':
    n = 4
    case = Solution()
    res =  case.solveNQueens(n)
    for i in res:
        print i
