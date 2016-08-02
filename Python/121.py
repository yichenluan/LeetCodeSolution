class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        preProfit = 0
        minProfit = prices[0]
        for i in range(1, len(prices)):
            nowProfit = max(preProfit, prices[i] - minProfit)
            if prices[i] < minProfit:
                minProfit = prices[i]
            preProfit = nowProfit
        return preProfit
