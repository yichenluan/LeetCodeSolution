class Solution(object):
    def deleteDuplicates(self, head):
        currNode = head
        while currNode:
            currVal = currNode.val
            nextNode = currNode.next
            if not nextNode:
                break
            nextVal = nextNode.val
            if nextVal == currVal:
                currNode.next = nextNode.next
            else:
                currNode = currNode.next
        return head
