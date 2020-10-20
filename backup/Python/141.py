class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        fast = head.next.next
        slow = head.next
        while fast != slow:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
            if slow:
                slow = slow.next
            else:
                return False
        return True
