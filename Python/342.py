class Solution(object):
    def isPowerOfFour(self, num):
        if not num:
            return False
        if not (num & (num - 1)) == 0:
            return False
        if not (num - 1) % 3 == 0:
            return False
        return True
