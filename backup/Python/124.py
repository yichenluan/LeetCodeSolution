class Solution(object):
    maxsum = float('-inf')
    def maxPathSum(self, root):
        def dfs(root):
            if not root:
                return 0
            leftToRoot = max(0, dfs(root.left))
            rightToRoot = max(0, dfs(root.right))

            self.maxsum = max(self.maxsum, leftToRoot + root.val + rightToRoot)
            return max(leftToRoot, rightToRoot) + root.val

        dfs(root)
        return self.maxsum
