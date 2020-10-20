class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for s in tokens:
            if s in '+-*/':
                op2 = stack.pop()
                op1 = stack.pop()
                if s == '+':
                    stack.append(op1+op2)
                elif s == '-':
                    stack.append(op1-op2)
                elif s == '*':
                    stack.append(op1*op2)
                else:
                    sign = -1 if (op1<0) ^ (op2<0) else 1
                    stack.append(abs(op1)/abs(op2) * sign)
            else:
                stack.append(int(s))
        return stack[-1]
