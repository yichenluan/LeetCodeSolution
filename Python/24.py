class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head and head.next:
            node = head
            pre.next = node.next
            node.next = pre.next.next
            pre.next.next = node
            head = node.next
            pre = node
        return dummy.next
