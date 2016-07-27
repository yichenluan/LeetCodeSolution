import ctypes
class Solution(object):
    def getSum(self, a, b):
        sum = 0
        carry = ctypes.c_int(b)
        while carry.value != 0:
            sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = sum
        return sum

if __name__ == '__main__':
    test = Solution()
    a = -1
    b = 1
    print test.getSum(a, b)
