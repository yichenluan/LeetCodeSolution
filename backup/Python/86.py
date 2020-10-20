class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        lessList = ListNode(0)
        greaterList = ListNode(0)
        less = lessList
        greater = greaterList
        while head:
            nextNode = head.next
            if head.val < x:
                lessList.next = head
                lessList.next.next = None
                lessList = head
            else:
                greaterList.next = head
                greaterList.next.next = None
                greaterList = head
            head = nextNode
        if not less.next:
            return greater.next
        else:
            lessList.next = greater.next
            return less.next
