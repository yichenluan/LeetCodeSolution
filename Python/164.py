class Solution(object):
    def maximumGap(self, nums):

        def radixsort(nums):
            idx, bits = 0, 32
            while idx < bits:
                zeroes, ones = [], []
                for num in nums:
                    if num & (1 << idx):
                        ones.append(num)
                    else:
                        zeroes.append(num)
                nums = zeroes + ones
                idx += 1
            return nums
        nums = radixsort(nums)
        return max([b-a for a, b in zip(nums, nums[1:])] or [0])


class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        maxV, minV = max(nums), min(nums)
        maxGap = (maxV - minV) // (len(nums) - 1)
        bSize = maxGap + 1
        buckets = [[] for _ in range((maxV - minV) // bSize + 1)]
        for n in num:
            buckets[(n-minV) // bSize].append(n)
        buckets = [b for b in buckets if b]
        for i in range(1, len(buckets)):
            maxGap = max(maxGap, min(buckets[i]) - max(buckets[i-1]))
        return maxGap
