class Solution(object):
    def reverse(self, x):
        negative = x < 0
        reversed = int(str(abs(x))[::-1])
        if reversed > 2147483647:
            return 0
        if negative:
            return -reversed
        return reversed
