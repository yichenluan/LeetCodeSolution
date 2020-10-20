class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        if self.getDepth(root.left) - self.getDepth(root.right) in (0, 1, -1):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
