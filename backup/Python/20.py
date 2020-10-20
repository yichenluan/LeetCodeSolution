class Solution(object):
    def isValid(self, s):
        validStack = list()
        validDict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            validStack.append(char)
            if len(validStack) >= 2 and validDict.get(validStack[-1]) == validStack[-2]:
                validStack.pop()
                validStack.pop()
        return validStack == []


if __name__ == '__main__':
    s = '()'
    case = Solution()
    print case.isValid(s)
