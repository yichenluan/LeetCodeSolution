class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        dp = [[]] * (n + 1)
        dp[1] = ['0', '1']
        for i in range(2, n + 1):
            dp[i] = [('0' + ins) for ins in dp[i-1]] + [('1' + ins) for ins in dp[i-1][::-1]]
        res = list()
        for ins in dp[n]:
            num = 0
            bits = ins[::-1]
            for i in range(len(bits)):
                num += (int(bits[i]) * (2 ** i))
            res.append(num)
        return res
