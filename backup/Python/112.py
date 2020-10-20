class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        treeQueue = [root]
        while treeQueue:
            temp = treeQueue.pop()
            if temp.left is None and temp.right is None:
                return temp.val == sum
            else:
                if temp.right:
                    temp.right.val += temp.val
                    treeQueue.append(temp.right)
                if temp.left:
                    temp.left.val += temp.val
                    treeQueue.append(temp.left)
        return False
