class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return None
        dummy = ListNode(-9999)
        dummy.next = head
        curr = head
        pre = dummy
        while curr:
            node = curr
            pre.next = curr.next
            begin = dummy
            if pre.val > node.val:
                while begin.next.val < node.val and begin != pre:
                    begin = begin.next
            node.next = begin.next
            begin.next = node
            # ..
            if pre.next == node:
                pre = node
                curr = node.next
            else:
                curr = pre.next
        return dummy.next


class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return None
        helper = ListNode(0)
        cur = head
        pre = helper
        nextNode = None
        while cur:
            nextNode = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = helper
            cur = nextNode
        return helper.next
