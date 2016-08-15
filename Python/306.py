class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                if self.isValid(i, j, num):
                    return True
        return False

    def isValid(self, i, j, num):
        if (num[0] == '0' and i>1) or (num[i] == '0' and j-i > 1):
            return False
        num1 = int(num[:i])
        num2 = int(num[i:j])
        start = j
        while start != len(num):
            sumNum = num1 + num2
            sumStr = str(sumNum)
            sumLen = len(sumStr)
            if num[start:start+sumLen] != sumStr:
                return False
            num1 = num2
            num2 = sumNum
            start = start + sumLen
        return True


if __name__ == '__main__':
    num = '1023'
    case = Solution()
    print case.isAdditiveNumber(num)
