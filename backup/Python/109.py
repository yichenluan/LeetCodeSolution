class Solution(object):
    def sortedListToBST(self, head):
        n = 0
        if not head:
            return None
        if head.next == None:
            res =  TreeNode(head.val)
            return res
        slow_p = head
        fast_p = head.next.next
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        midNode = TreeNode(slow_p.next.val)
        right = self.sortedListToBST(slow_p.next.next)
        slow_p.next = None
        left = self.sortedListToBST(head)
        midNode.left = left
        midNode.right = right
        return midNode

