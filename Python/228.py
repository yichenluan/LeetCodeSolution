class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = list()
        left = None
        right = None
        pre = None
        for i in xrange(len(nums)):
            curr = nums[i]
            if left is None:
                left = curr
            if curr == left or curr == pre + 1:
                right = curr
            else:
                if left == right:
                    res.append(str(left))
                else:
                    res.append(str(left) + '->' + str(right))
                left = curr
                right = left
            pre = curr
        if left == right:
            res.append(str(left))
        else:
            res.append(str(left) + '->' + str(right))
        return res
