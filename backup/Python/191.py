class Solution(object):
    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            case = 2 ** i
            if case > n:
                break
            if case & n > 0:
                res += 1
        return res


class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
