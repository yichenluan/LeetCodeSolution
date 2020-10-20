class Solution(object):
    def kthSmallest(self, root, k):
        stack = list()
        sort_list = list()
        stack.append(root)
        curr = root
        while stack:
            while curr.left:
                stack.append(curr.left)
                curr = curr.left
            node = stack.pop()
            sort_list.append(node.val)
            if len(sort_list) == k:
                return sort_list.pop()
            if node.right:
                stack.append(node.right)
                curr = node.right
        return sort_list.pop()


class Solution(object):
    def kthSmallest(self, root, k):
        count = 0
        val = 0
        self.kthHandler(root, count, k, val)
        return val
    
    def kthHandler(self, root, count, k, val):
        if root == None:
            return None
        self.kthHandler(root.left, count, k, val)
        count += 1
        if count == k:
            val = root.val
        self.kthHandler(root.right, count, k, val)
