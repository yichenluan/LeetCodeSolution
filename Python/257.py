class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = list()

        def dfs(node, currPath):
            if not node.left and not node.right:
                res.append(currPath)
                return
            if node.left:
                dfs(node.left, currPath+'->'+str(node.left.val))
            if node.right:
                dfs(node.right, currPath+'->'+str(node.right.val))
        dfs(root, str(root.val))
        return res
