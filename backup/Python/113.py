class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = list()

        def dfs(root, curr, path):
            if root.left is None and root.right is None:
                if curr == sum:
                    res.append(path)
                return
            if root.left:
                dfs(root.left, curr+root.left.val, path+[root.left.val])
            if root.right:
                dfs(root.right, curr+root.right.val, path+[root.right.val])
        
        dfs(root, root.val, [root.val])
        return res
