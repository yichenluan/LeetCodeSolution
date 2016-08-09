class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
