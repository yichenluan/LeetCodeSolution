class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        if (root.val >= p.val and root.val <= q.val) or(root.val <= p.val and root.val >= q.val):
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
