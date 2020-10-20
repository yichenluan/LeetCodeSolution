class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        p_first = head
        p_second = head
        while n:
            p_first = p_first.next
            n -= 1
        if not p_first:
            return head.next
        while p_first.next:
            p_second = p_second.next
            p_first = p_first.next
        p_second.next = p_second.next.next
        return head
