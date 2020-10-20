class Solution(object):
    def reorderList(self, head):
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
