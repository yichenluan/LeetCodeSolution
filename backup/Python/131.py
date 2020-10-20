class _Solution(object):
    def partition(self, s):
        return [[s[:i]] + rest
                for i in xrange(1, len(s)+1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition(s[i:])] or [[]]


class Solution(object):
    def partition(self, s):
        if not s:
            return [[]]
        res = list()
        for i in xrange(1, len(s) + 1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    res.append([s[:i]] + rest)
        return res


if __name__ == '__main__':
    s = 'aab'
    case = Solution()
    print case.partition(s)
