class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        left = 0
        right = n - 1
        key = 0
        while left <= right:
            mid = (left + right) / 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                key = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = left + 1
        m = len(matrix[key])
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) / 2
            if matrix[key][mid] == target:
                return True
            if matrix[key][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == '__main__':
    matrix = [[1, 3]]
    target = 3
    case = Solution()
    print case.searchMatrix(matrix, target)
