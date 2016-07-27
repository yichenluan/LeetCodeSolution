class Solution(object):
    def countBits(self, num):
        res = list()
        count = 0
        for i in range(num+1):
            if i == 0:
                res.append(0)
            elif i == 1:
                count = 2**i
                res.append(1)
            elif i == count:
                near_num = i
                res.append(1)
                count = 2 * count
            else:
                res.append(1 + res[i - near_num])
        return res


if __name__ == '__main__':
    testCase = 8
    test = Solution()
    print test.countBits(testCase)
