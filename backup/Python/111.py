class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        depthRes = list()
        stack = [(root, 1)]
        while stack:
            node_val = stack.pop()
            node = node_val[0]
            if not node.left and not node.right:
                depthRes.append(node_val[1])
            if node.right:
                stack.append((node.right, node_val[1] + 1))
            if node.left:
                stack.append((node.left, node_val[1] + 1))
        return min(depthRes)
            
