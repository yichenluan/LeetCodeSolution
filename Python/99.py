class Solution(object):
    def recoverTree(self, root):
        self.first, self.second, self.pre = None, None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.dfs(root.right)


#iteratively
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack,virgin = [], True
        first, second, pre = None, None, None
        while True:
            while (root != None):
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if pre != None and pre.val > node.val:
                if virgin:
                    first = pre
                    virgin = False
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val
