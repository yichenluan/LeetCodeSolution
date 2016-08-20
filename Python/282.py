class Solution(object):
    def addOperators(self, num, target):
        
        def handler(num, candidate):
            if not num:
                if eval(candidate) == target:
                    res.append(candidate)
                return
            for i in range(1, len(num) + 1):
                if num[0] == '0' and i > 1:
                    continue
                handler(num[i:], candidate + '+' + num[:i])
                handler(num[i:], candidate + '-' + num[:i])
                handler(num[i:], candidate + '*' + num[:i])

        res = list()

        for i in range(1, len(num) + 1):
            handler(num[i:], num[:i])
        return res



if __name__ == '__main__':
    num = '123'
    target = 6
    case = Solution()
    print case.addOperators(num, target)
