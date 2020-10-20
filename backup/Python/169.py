class Solution(object):
    def majorityElement(self, nums):
        l = list(nums)
        l.sort()
        return l[len(l) / 2]
