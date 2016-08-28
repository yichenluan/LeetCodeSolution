class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        maxEndingHere = nums[0]
        minEndingHere = nums[0]
        for i in xrange(1, len(nums)):
            maxTemp = maxEndingHere
            maxEndingHere = max(maxEndingHere * nums[i], nums[i], minEndingHere * nums[i])
            minEndingHere = min(minEndingHere * nums[i], nums[i], maxTemp * nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
