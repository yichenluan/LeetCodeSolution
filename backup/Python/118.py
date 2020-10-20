class Solution(object):
    def generate(self, numRows):
        res = list()
        if numRows >= 1:
            res.append([1])
        if numRows >= 2:
            res.append([1, 1])
        for i in range(2, numRows):
            beforeRow = res[-1]
            nowRow = [1]
            for j in range(1, i):
                nowRow.append(beforeRow[j - 1] + beforeRow[j])
            nowRow.append(1)
            res.append(nowRow)
        return res
