class Solution(object):
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            b = (n>>i) & 1
            ret += b<<(31-i)
        return ret
