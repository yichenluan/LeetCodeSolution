class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        x_start = 0
        y_start = 0
        step = n - 1
        while step > 0:
            temp = list()
            nextTemp = list()
            temp_x_start = x_start
            temp_y_start = y_start
            for i in range(step):
                temp.append(matrix[x_start][y_start])
                y_start += 1
            for i in range(step):
                nextTemp.append(matrix[x_start][y_start])
                matrix[x_start][y_start] = temp[i]
                x_start += 1
            temp = nextTemp
            nextTemp = list()
            for i in range(step):
                nextTemp.append(matrix[x_start][y_start])
                matrix[x_start][y_start] = temp[i]
                y_start -= 1
            temp = nextTemp
            nextTemp = list()
            for i in range(step):
                nextTemp.append(matrix[x_start][y_start])
                matrix[x_start][y_start] = temp[i]
                x_start -= 1
            temp = nextTemp
            nextTemp = list()
            for i in range(step):
                matrix[temp_x_start][temp_y_start] = temp[i]
                temp_y_start += 1
            x_start += 1
            y_start += 1
            step -= 2
        print matrix


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    case = Solution()
    case.rotate(matrix)
