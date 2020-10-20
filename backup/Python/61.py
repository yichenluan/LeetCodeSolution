class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return []
        length, curr = 1, head
        while curr.next:
            length += 1
            curr = curr.next
        k %= length

        curr.next = head

        for i in xrange(length -k -1):
            head = head.next

        last = head
        head = head.next
        last.next = None

        return head
