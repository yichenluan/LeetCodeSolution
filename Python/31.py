class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                self.reverse(nums, i, len(nums)-1)
                c = i - 1
                for j in range(i, len(nums)):
                    if nums[j] > nums[c]:
                        nums[c], nums[j] = nums[j], nums[c]
                        return
    
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
