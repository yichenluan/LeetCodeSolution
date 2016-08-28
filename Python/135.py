class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        can = [1] * n
        for i in range(n -1):
            if ratings[i+1] > ratings[i]:
                can[i+1] = can[i] + 1
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i] and can[i-1] < (can[i] + 1):
                can[i-1] = can[i] + 1
        return sum(can)

