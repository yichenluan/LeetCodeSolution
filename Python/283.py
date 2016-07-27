'''
弱者的解法
'''
class Solution(object):
    def moveZeroes(self, nums):
        zero_point = 0
        num_point = 0
        nums_len = len(nums)
        while zero_point < nums_len - 1:
            flag = False
            for i in range(zero_point, nums_len):
                if nums[i] == 0:
                    zero_point = i
                    flag = True
                    break
            if not flag:
                break
            flag = False
            for i in range(zero_point, nums_len):
                if nums[i] != 0:
                    num_point = i
                    flag = True
                    break
            if not flag:
                break
            nums[zero_point], nums[num_point] = nums[num_point], nums[zero_point]
            zero_point = num_point = zero_point + 1


'''
正确的解法
'''
class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for num in nums:
            if num != 0:
                nums[count] = num
                count += 1
        for index in range(count, len(nums)):
            nums[index] = 0
