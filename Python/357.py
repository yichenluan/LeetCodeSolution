class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        ans = 10
        base = 9
        for i in range(2, (n+1)):
            if i > 10:
                break
            base = base * (9 - i + 2)
            ans += base
        return ans
