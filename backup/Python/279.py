class _Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        lst = [i*i for i in range(1, int(n ** 0.5) + 1)]
        res = 0
        toCheck = [n]
        while toCheck:
            res += 1
            temp = list()
            while toCheck:
                i = toCheck.pop()
                for j in lst:
                    if i == j:
                        return res
                    if i < j:
                        break
                    temp.append(i-j)
            toCheck = temp
        return res


if __name__ == '__main__':
    n = 4
    case = Solution()
    print case.numSquares(n)
