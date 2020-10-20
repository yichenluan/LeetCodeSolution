class Solution(object):
    def levelOrder(self, root):
        res = list()
        if not root:
            return res
        nodeQueue = [root]
        while nodeQueue:
            tempQueue = list()
            valueList = list()
            while nodeQueue:
                node = nodeQueue.pop()
                valueList.append(node.val)
                if node.left:
                    tempQueue.insert(0, node.left)
                if node.right:
                    tempQueue.insert(0, node.right)
            res.append(valueList)
            nodeQueue = tempQueue
        return res
