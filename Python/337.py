class Solution(object):
    def rob(self, root):
        def dfs(root):
            if not root:
                return (0, 0)
            leftpre, leftppre = dfs(root.left)
            rightpre, rightppre = dfs(root.right)
            ppre = leftpre + rightpre
            pre = max(root.val + leftppre + rightppre, ppre)
            return pre, ppre
        return dfs(root)[0]
