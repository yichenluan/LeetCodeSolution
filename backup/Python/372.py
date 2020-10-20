class Solution(object):
    def superPow(self, a, b):
        num = int(''.join([str(n) for n in b]))

        a %= 1337
        result = 1
        while num > 0:
            if num % 2 == 1:
                result = (result * a) % 1337
            num = num >> 1
            a = (a * a) % 1337
        return result
