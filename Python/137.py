'''Single Number II

https://discuss.leetcode.com/topic/22821/an-general-way-to-handle-all-this-sort-of-questions
这个解法很强。。。
'''
class Solution(object):
    def singleNumber(self, nums):
        r = 0
        for i in range(32):
            bit = 0
            for num in nums:
                if num & (1 << i): bit += 1
            bit %= 3
            if i != 31: r += bit << i
    	    elif bit == 1: r -= (1 << 31)
        return r   
