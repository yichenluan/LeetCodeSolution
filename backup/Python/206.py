class Solution(object):
    def reverseList(self, head):
        res = None
        while head:
            temp = head
            head = head.next
            temp.next = res
            res = temp
        return res


class Solution(object):
    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, head, new):
        if head == None:
            return new
        temp = head.next
        head.next = new
        return self.reverse(temp, head)
