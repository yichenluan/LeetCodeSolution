import operator
class Solution(object):
    cache = dict()
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    def diffWaysToCompute(self, input):
        ans = list()
        if input in self.cache:
            return self.cache[input]
        for idx in xrange(len(input)):
            oper = input[idx]
            if oper in self.ops:
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx+1:])
                for l in left:
                    for r in right:
                        ans.append(self.ops[oper](l, r))
                self.cache[input] = ans
        if not ans:
            ans.append(int(input))
        return ans
