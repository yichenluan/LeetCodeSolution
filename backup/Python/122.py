class Solution(object):
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices) - 1):
            res += max(prices[i + 1] - prices[i])
        return res
