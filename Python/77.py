class Solution(object):
    def combine(self, n, k):
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        first = [i + [n] for i in self.combine(n-1, k-1)]
        second = [i for i in self.combine(n-1, k)]
        return first + second
