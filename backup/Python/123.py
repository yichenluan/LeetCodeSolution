'''
https://discuss.leetcode.com/topic/52532/dp-o-n-run-time-beginner-code-nothing-fancy-thinking-process-and-well-commented
'''
class Solution(object):
    def maxProfit(self, p):
        if not p: return 0
        sell, buyd, n, minp, maxp = [0], [0], len(p), p[0], p[-1]
        for i in range(1, n):
            minp, maxp = min(minp, p[i]), max(maxp, p[n-i-1])
            sell.append(max(sell[i-1], p[i] - minp))
            buyd.append(max(buyd[i-1], maxp - p[n-i-1]))
        return max(sell[i] + buyd[n-i-1] for i in range(n))

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)<=1): return 0
        b1=-prices[0]
        s1=0
        b2=-prices[0]
        s2=0
        for i in xrange(1,len(prices)):
            p=prices[i]
            s2=max(s2,b2+p)
            b2=max(b2,s1-p)
            s1=max(b1+p,s1)
            b1=max(b1,-p)
            
        return max(s1,s2)
