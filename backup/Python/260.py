'''Single Number III

重点在于如何区分出不同的两个数，全部异或可以去到两个数所有不同的比特位
然后，xor & -xor 可以取到唯一一位不同bit的位置，这样就可以求解了。
'''
class Solution(object):
    def singleNumber(self, nums):
        xor = reduce((lambda x, y: x ^ y), nums)
        low_bit = xor & -xor
        a = b =0
        for num in nums:
            if num & low_bit:
                a ^= num
            else:
                b ^= num
        return a, b
