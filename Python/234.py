class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
