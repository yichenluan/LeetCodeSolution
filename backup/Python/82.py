class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy.next
        pre = dummy
        while node:
            duplicate = False
            val = node.val
            curr = node
            while curr.next and curr.next.val == val:
                duplicate = True
                curr = curr.next
            if duplicate:
                pre.next = curr.next
            else:
                pre = node
            node = curr.next
        return dummy.next

