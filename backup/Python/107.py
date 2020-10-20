class Solution():
    def levelOrderBottom(self, root):
        if not root:
            return []
        res = list()
        nodeStack = list()
        nodeStack.append(root)
        while nodeStack:
            nextStack = list()
            temp = list()
            while nodeStack:
                node = nodeStack.pop()
                temp.append(node.val)
                if node.right:
                    nextStack.insert(0, node.right)
                if node.left:
                    nextStack.insert(0, node.left)
            res.append(temp[::-1])
            nodeStack = nextStack
        return res[::-1]
