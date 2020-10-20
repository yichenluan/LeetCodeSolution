class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p = ListNode(-1)
        dummy = p
        val = 0
        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            p.next = ListNode(val % 10)
            val /= 10
            p = p.next
        return dummy.next
