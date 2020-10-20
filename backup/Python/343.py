class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        a = n % 3
        b = n / 3
        if a == 0:
            res = 3 ** b
        elif a == 1:
            a += 3
            b -= 1
            res = a * (3 ** b)
        else:
            res = a * (3 ** b)
        return res
