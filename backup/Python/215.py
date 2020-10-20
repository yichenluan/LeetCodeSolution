class Solution(object):
    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1


    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left
        r = right
        while l < r:
            while nums[r] <= pivot and l < r:
                r -= 1
            while nums[l] >= pivot and l < r:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[left], nums[l] = nums[l], nums[left]
        return l
