class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        now = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return now + left + right


class Solution(object):
    def preorderTraversal(self, root):
        res = list()
        stack = list()
        stack.append(root)
        while stack:
            currNode = stack.pop()
            if currNode:
                res.append(currNode.val)
                stack.append(currNode.right)
                stack.append(currNode.left)
        return res
