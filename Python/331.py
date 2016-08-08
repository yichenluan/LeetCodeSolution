class Solution(object):
    def isValidSerialization(self, preorder):
        if not preorder:
            return False
        preorder = preorder.split(',')
        count = 1
        i = 0
        while i < len(preorder):
            if preorder[i] == '#':
                count -= 1
            else:
                count += 1
            if i!= len(preorder) - 1 and count == 0:
                return False
            i += 1
        return count ==0


class Solution(object):
    def isValidSerialization(self, preorder):
        stack = list()
        for item in preorder.split(','):
            stack.append(item)
            while len(stack) >= 3 and \
                    stack[-1] == stack[-2] == '#' and \
                    stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'
