class Solution(object):
    def connect(self, root):
        if not root:
            return root
        nodeQueue = list()
        nodeQueue.append(root)
        while nodeQueue:
            nextQueue = list()
            currNode = None
            while nodeQueue:
                node = nodeQueue.pop()
                node.next = currNode
                currNode = node
                if node.right:
                    nextQueue.insert(0, node.right)
                if node.left:
                    nextQueue.insert(0, node.left)
            nodeQueue = nextQueue

