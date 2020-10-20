class Solution(object):
    def plusOne(self, digits):
        flag = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            digit = digits[i]
            val = flag + digit
            if val < 10:
                digits[i] = val
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

