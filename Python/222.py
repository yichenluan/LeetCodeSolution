class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l > r:
            return self.countNodes(root.left) + (1 << r);
        else:
            return self.countNodes(root.right) + (1 << l);

    def height(self, root):
        depth = 0
        while root:
            root = root.left
            depth += 1
        return depth
