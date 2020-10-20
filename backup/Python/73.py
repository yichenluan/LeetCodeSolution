class Solution(object):
    def setZeroes(self, matrix):
        x_len = len(matrix)
        if not x_len:
            return 
        y_len = len(matrix[0])
        first_x = False
        first_y = False
        for i in range(y_len):
            if matrix[0][i] == 0:
                first_x = True
                break
        for i in range(x_len):
            if matrix[i][0] == 0:
                first_y = True
                break
        for i in range(1, x_len):
            for j in range(1, y_len):
                if matrix[i][j]== 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, x_len):
            if matrix[i][0] == 0:
                for j in range(y_len):
                    matrix[i][j] = 0
        for i in range(y_len):
            if matrix[0][i] == 0:
                for j in range(x_len):
                    matrix[j][i] = 0
        if first_x:
            for i in range(y_len):
                matrix[0][i] = 0
        if first_y:
            for i in range(x_len):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    case = Solution()
    print case.setZeroes(matrix)
