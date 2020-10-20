class Solution(object):
    def generateTrees(self, n):

        def handler(begin, end):
            res = list()
            for num in range(begin, end+1):
                leftTree = handler(begin, num-1)
                rightTree = handler(num+1, end)
                for i in leftTree:
                    for j in rightTree:
                        root = TreeNode(num)
                        root.left = i
                        root.right = j
                        res += [root]
            return res or [None]

        if n == 0:
            return []
        return handler(1, n)
