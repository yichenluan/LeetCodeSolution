class Solution(object):
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        odd_begin, even_begin = odd, even
        head = even.next
        oddFlag = True
        while head:
            if oddFlag:
                odd.next = head
                odd = head
                oddFlag = False
            else:
                even.next = head
                even = head
                oddFlag = True
            head = head.next
        odd.next = even_begin
        even.next = None
        return odd_begin
