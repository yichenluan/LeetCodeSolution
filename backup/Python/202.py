class Solution(object):
    def isHappy(self, n):
        case = list()
        while True:
            if n in case:
                return False
            case.append(n)
            new_n = 0
            while n:
                new_n += (n % 10) ** 2
                n = n / 10
            if new_n == 1:
                return True
            else:
                n = new_n
