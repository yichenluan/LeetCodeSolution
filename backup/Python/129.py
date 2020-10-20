class Solution(object):
    resList = list()

    def sumNumbers(self, root):
        self.resList = list()
        if not root:
            return 0
        self.dfs(root, '')
        res = [int(s) for s in self.resList]
        return sum(res)


    def dfs(self, root, s):
        s += str(root.val)
        if not root.left and not root.right:
            self.resList.append(s)
            return
        
        if root.left:
            self.dfs(root.left, s)
        if root.right:
            self.dfs(root.right, s)

