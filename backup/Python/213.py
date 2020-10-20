class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
                return 0
        if len(nums)<=2 and len(nums) != 0:
            return max(nums)
        
        # 利用House Robber中的方法
        def last_rob(nums):
            if len(nums) == 0:
                return 0
            if len(nums)<=2 and len(nums) != 0:
                return max(nums)
            # 动态规划
            mynum = [nums[0],max(nums[0],nums[1])]    # 使用一个list记录到当前位置最大的值
            for i in xrange(2,len(nums)):
                max_num = nums[i]+mynum[-2]
                if max_num >= mynum[-1]:
                    mynum.append(max_num)
                else:
                    mynum.append(mynum[-1])
            return mynum[-1]
        # 从第一个开始到倒数第二个字符，或从第二个开始到最后一个字符。分两种情况。时间复杂度O(n)
        return max(last_rob(nums[0:len(nums)-1]),last_rob(nums[1:len(nums)]))    
