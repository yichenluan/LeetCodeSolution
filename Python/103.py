class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        nodeQueue = [root]
        res = list()
        flag = True
        while nodeQueue:
            temp = list()
            nextQueue = list()
            while nodeQueue:
                node = nodeQueue.pop()
                temp.append(node.val)
                if node.left:
                    nextQueue.insert(0, node.left)
                if node.right:
                    nextQueue.insert(0, node.right)
            if not flag:
                temp.reverse()
                flag = True
            else:
                flag = False
            res.append(temp)
            nodeQueue = nextQueue
        return res
