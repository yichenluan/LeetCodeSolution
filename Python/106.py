class Solution(object):
    def buildTreeT(self, inorder, postorder, s1, e1, s2, e2):
        if e2-s2 <= 0:
            return None
    
        node = TreeNode(postorder[e2-1])
        i = s1
        while i < e1:
            if inorder[i] == node.val:
                break
            i += 1

        node.left = self.buildTreeT(inorder, postorder, s1, i, s2, (s2+(i-s1)))
        node.right = self.buildTreeT(inorder, postorder, i+1, e1, (s2+(i-s1)), e2-1)
        return node

    def buildTree(self, inorder, postorder):
        return self.buildTreeT(inorder, postorder, 0, len(inorder), 0, len(postorder))


class Solution(object):
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		length = len(inorder)
		if length == 0:
			return None
		if length == 1:
			return TreeNode(inorder[0])

		root = TreeNode(None)
		stack = [ (root, 0, length-1, length) ]
		while stack:
			# in_s (po_e): start (end) index of the "sub"-inorder (postorder)
			node, in_s, po_e, size = stack.pop()
			val = postorder[po_e]
			node.val = val
			idx = inorder.index(val)
			# size of the left node
			lsize = idx - in_s
			# size of the right node
			rsize = size - lsize - 1
			if rsize == 0:
				node.right = None
			elif rsize == 1:
				node.right = TreeNode(postorder[po_e - 1])
			else:
				node.right = TreeNode(None)
				stack.append( (node.right, idx+1, po_e-1, rsize) )
			if lsize == 0:
				node.left = None
			elif lsize == 1:
				node.left = TreeNode(postorder[po_e - 1 - rsize])
			else:
				node.left = TreeNode(None)
				stack.append( (node.left, in_s, po_e - 1 - rsize, lsize) )
		return root
