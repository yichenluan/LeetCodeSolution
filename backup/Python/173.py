class BSTIterator(object):
    def __init__(self, root):
        self.visit = root
        nodeStack = list()

    def hasNext(self):
        return not visit or not nodeStack

    def next(self):
        while self.visit:
            nodeStack.append(self.visit)
            self.visit = self.visit.left
        node = nodeStack.pop()
        self.visit = node.right
        return node.val
