class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        res = [0] * n
        sortedNums = list()

        def binarySearch(target):
            l = 0
            r = len(sortedNums)
            while l < r:
                m = (l + r) / 2
                if sortedNums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        for i in range(n-1, -1, -1):
            idx = binarySearch(nums[i])
            res[i] = idx
            sortedNums.insert(idx, nums[i])
        return res
