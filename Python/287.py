class Solution(object):
    def findDuplicate(self, nums):
        fast = 0
        slow = 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
