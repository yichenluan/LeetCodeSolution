class Solution(object):
    def minPatches(self, nums, n):
        coverdSum = list()
        for num in nums:
            temp = [num] + [nu + num for nu in coverdSum]
            for t in temp:
                if t not in coverdSum:
                    coverdSum.append(t)
        res = 0
        while True:
            firstNotCoverd = 0
            for i in range(1, n+1):
                if i not in coverdSum:
                    firstNotCoverd = i
                    break
            if not firstNotCoverd:
                return res
            res += 1
            temp = [firstNotCoverd] + [nu+firstNotCoverd for nu in coverdSum]
            for num in temp:
                if num not  in coverdSum:
                    coverdSum.append(num)


class Solution(object):
    def minPatches(self, nums, n):
        miss = 1
        added = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added


if __name__ == '__main__':
    nums = [1, 5, 10]
    n = 20
    case = Solution()
    print case.minPatches(nums, n)
