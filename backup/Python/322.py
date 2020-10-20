class Solution(object):
    def coinChange(self, coins, amount):
        need = [(amount+1) for _ in range(amount + 1)]
        need[0] = 0
        for c in coins:
            for a in xrange(c, amount+1):
                need[a] = min(need[a], 1+need[a-c])

        if need[-1] > amount:
            return -1
        else:
            return need[-1]
