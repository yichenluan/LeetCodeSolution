class Solution(object):
    def mergeKLists(self, lists):
        def merge(lst1, lst2):
            dummy = pt = ListNode(-1)
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    pt.next = lst1
                    lst1 = lst1.next
                else:
                    pt.next = lst2
                    lst2 = lst2.next
                pt = pt.next
            pt.next = lst1 or lst2
            return dummy.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)
