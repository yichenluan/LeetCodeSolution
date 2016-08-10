class Solution(object):
    def getIntersectionNode(self, headA, headB):
        stackA = list()
        stackB = list()
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next

        pre = None

        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            if nodeA == nodeB:
                pre = nodeA
            else:
                break
        return pre


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        len_a = 0
        len_b = 0
        p_a = headA
        p_b = headB
        while p_a:
            len_a += 1
            p_a = p_a.next
        while p_b:
            len_b += 1
            p_b = p_b.next
        p_a = headA
        p_b = headB
        for i in range(len_a - len_b):
            p_a = p_a.next
        for i in range(len_b - len_a):
            p_b = p_b.next

        while p_b:
            if p_a == p_b:
                return p_a
            p_a = p_a.next
            p_b = p_b.next
        return None
