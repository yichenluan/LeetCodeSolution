class Solution(object):
    def getRow(self, numRows):
        res = list()
        if numRows ==0:
            return [1]
        if numRows == 1:
            return [1, 1]
        ans = list()
        beforeRow = [1, 1]
        for i in range(2, numRows + 1):
            nowRow = [1]
            for j in range(1, i):
                nowRow.append(beforeRow[j - 1] + beforeRow[j])
            nowRow.append(1)
            beforeRow = nowRow
            ans = nowRow
        return ans
