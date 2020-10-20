class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            res = num % 9
            if res == 0:
                res = 9
            return res
