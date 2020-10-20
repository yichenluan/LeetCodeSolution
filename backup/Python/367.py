class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num - 1
        while left < right:
            mid = left + (right - left) / 2
            mid_squre = mid * mid
            if mid_squre == num:
                return True
            if mid_squre > num:
                right = mid - 1
            else:
                left = mid + 1
        if left * left == num:
            return True
        else:
            return False
