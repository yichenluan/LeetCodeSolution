class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r, five = 0, 5
        c = n/five
        while c>0:
            r += c
            five *= 5
            c = n/five
        return r
