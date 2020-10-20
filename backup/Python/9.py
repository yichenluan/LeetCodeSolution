class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        xx = x
        y = 0
        while xx:
            y = y * 10 + xx % 10
            xx /= 10
        return y == x
