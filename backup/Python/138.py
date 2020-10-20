class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        curr = head
        while curr:
            temp = RandomListNode(curr.label)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        copy = RandomListNode(0)
        origin = RandomListNode(0)
        copyDummy = copy
        originDummpy = origin
        flag = True
        curr = head
        while curr:
            if flag:
                origin.next = curr
                flag = False
            else:
                copy.next = curr
                flag = True
            curr = curr.next
        origin.next = None
        copy.next = None
        head = originDummpy.next
        return copyDummy.next
