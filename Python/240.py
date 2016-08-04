class Solution(object):
    def searchMatrix(self, matrix, target):
        x = len(matrix)
        y = len(matrix[0])
        i = x - 1
        j = 0
        while i >= 0 and j < y:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False
