class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        index = 0
        while index < m - 1:
            curr = curr.next
            index += 1
        reverse = None
        tail = curr.next
        while index < n:
            node = curr.next
            curr.next = node.next
            node.next = reverse
            reverse = node
            index += 1
        tail.next = curr.next
        curr.next = reverse
        return dummy.next
