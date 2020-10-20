class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        pre.next = None
        left = head
        right = slow
        self.sortList(left)
        self.sortList(right)
        res = self.merge(left, right)
        return res

    def merge(self, left, right):
        dummy = tail = ListNode(None)
        while left and right:
            if left.val < right.val:
                tail.next = left
                tail = left
                left = left.next
            else:
                tail.next = right
                tail = right
                right = right.next
        tail.next = left or right
        return dummy.next
