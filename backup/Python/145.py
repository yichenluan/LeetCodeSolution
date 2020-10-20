class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        curr = [root.val]
        return left + right + curr


class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res = list()
        nodeStack = list()
        curr = root
        pre = None
        while nodeStack or curr:
            while curr:
                nodeStack.append(curr)
                curr = curr.left
            lastNode = nodeStack[-1]
            if lastNode.right == None or lastNode.right == pre:
                pre = lastNode
                res.append(lastNode.val)
                nodeStack.pop()
            else:
                curr = lastNode.right
        return res
