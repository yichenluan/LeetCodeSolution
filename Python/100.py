class Solution(object):
    def isSameTree(self, p, q):
        if p == None or q == None:
            if p == q:
                return True
            else:
                return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
