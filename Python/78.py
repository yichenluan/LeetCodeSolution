class Solution(object):
    def subsets(self, nums):
        if not nums:
            return [[]]
        res = list()
        for num in nums:
            res += [i + [num] for i in res]
            res.append([num])
        res.append([])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    case = Solution()
    print case.subsets(nums)
