class Solution(object):
    def simplifypath(self, path):
        pathList = path.split('/')
        stack = []

        for elem in pathList:
            if elem == '..' and len(stack) != 0:
                stack.pop()
            elif elem != '.' and elem != '' and elem != '..':
                stack.append(elem)

        return '/' + '/'.join(stack)
