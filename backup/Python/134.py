class ListNode(object):
    def __init__(self, gas, cost, index):
        self.gas = gas
        self.cost = cost
        self.index = index
        self.next = None

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        dummy = ListNode(0, 0, -1)
        pre = dummy
        for i in range(len(gas)):
            node = ListNode(gas[i], cost[i], i)
            pre.next = node
            pre = node
        pre.next = dummy.next
        res = 0
        head = dummy.next
        curr = dummy.next
        while True:
            flag = False
            if curr.next == curr:
                return res
            while curr.next != head:
                if curr.gas > curr.cost:
                    flag = True
                    curr.gas = curr.gas - curr.cost + curr.next.gas
                    curr.cost = curr.next.cost
                    if curr.next == head:
                        head = curr.next.next
                    curr.next = curr.next.next
                else:
                    curr = curr.next
                    res = curr.index
            if not flag:
                return -1

# 上面的有问题

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalGas = 0
        totalCost = 0
        start = 0
        balance = 0
        for i in xrange(0, len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0
        if totalGas >= totalCost:
            return start
        return -1
