class Solution(object):
    def increasingTriplet(self, nums):
        smallest = sys.maxint
        secondSmallest = sys.maxint
        for num in nums:
            if num > secondSmallest:
                return True
            if num > smallest:
                secondSmallest = min(secondSmallest, num)
            smallest = min(smallest, num)
        return False
