class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        case = n - 1
        if n & case == 0:
            return True
        else:
            return False
