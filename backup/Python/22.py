class Solution(object):
    def generateParenthesis(self, n):
        res = list()
        s = ''
        self.build(n, 0, s, res)
        return res

    def build(self, remaining, left_open, s, res):
        if remaining == 0 and left_open == 0:
            res.append(s)
            return
        if remaining > 0:
            self.build(remaining - 1, left_open + 1, s + '(', res)
        if left_open > 0:
            self.build(remaining, left_open - 1, s+ ')', res)
