class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        nodeQueue = list()
        res = list()
        nodeQueue.append(root)
        while nodeQueue:
            res.append(nodeQueue[0].val)
            nextQueue = list()
            while nodeQueue:
                node = nodeQueue.pop()
                if node.left:
                    nextQueue.insert(0, node.left)
                if node.right:
                    nextQueue.insert(0, node.right)
            nodeQueue = nextQueue
        return res
