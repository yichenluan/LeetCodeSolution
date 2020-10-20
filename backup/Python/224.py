class Solution(object):
    def calculate(self, s):
        stack, result = [], 0
        num, sign = '', 1
        for c in s + '+':
            if c != ' ':
                if c in '+-':
                    result += int(num) * sign
                    sign = 1 if c == '+' else -1
                    num = ''
                elif c == '(':
                    stack.append(result)
                    stack.append(sign)
                    result, sign = 0, 1
                elif c == ')':
                    result += int(num) * sign
                    num = str(result)
                    sign = stack.pop()
                    result = stack.pop()
                else:
                    num += c
        return result
