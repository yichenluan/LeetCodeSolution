class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        result = 0
        # number of appearances for one cycle when 1 appears at position i
        i = 1
        while n >= i:
            # complete cycle, one more complete cycle if current digit > 1
            cycle = n / (i * 10) + (1 if n / i % 10 > 1 else 0)
            result += cycle * i
            # incomplete cycle if current digit == 1
            if n / i % 10 == 1:
                result += n % i + 1
            i *= 10
        return result
