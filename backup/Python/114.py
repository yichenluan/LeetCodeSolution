class Solution(object):
    def flatten(self, root):
        def handler(root):
            if not root:
                return root
            temp1 = self.flatten(root.left)
            temp2 = self.flatten(root.right)
            root.right = temp1
            root.left = None
            if temp1:
                while temp1.right:
                    temp1 = temp1.right
                temp1.right = temp2
            else:
                root.right = temp2
            return root
        root = handler(root)
