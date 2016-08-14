class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        if n < k:
            return head
        headNode = dummy
        curr = head
        tail = head
        reverse = None
        count = 0
        while True:
            if n < k:
                break
            headNode.next = curr.next
            curr.next = reverse
            reverse = curr
            curr = headNode.next
            count += 1

            if count == k:
                tail.next = headNode.next
                headNode.next = reverse

                reverse = None
                headNode = tail
                curr = headNode.next
                tail = headNode.next
                count = 0
                
                n -= k
        return dummy.next
