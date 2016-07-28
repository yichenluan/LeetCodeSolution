class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []
        left = self.inorderTraversal(root.left)
        value = [root.val]
        right = self.inorderTraversal(root.right)
        return left + value + right


class Solution(object):
    def inorderTraversal(self, root):
        res = list()
        stack = list()
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
