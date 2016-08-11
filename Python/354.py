class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
    
        l = len(envelopes)
        if l == 1:
            return 1
    
        envelopes.sort(
            cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1]) 
        # sort the envelopes by width because they need to be inorder before consider the heigths or versa
    
        width = []
        for i in envelopes:
            width.append(i[1])
        
        res = self.longestSubsequence(width)
        # the problem became LIS after sort(width)
    
        return res
    
    

    def longestSubsequence(self, nums):
        """
        return type: int (number of longest subsequence)
        """
        if not nums:
            return 0
        l = len(nums)
        res = []
    
        for num in nums:
            pos = self.binarySearch(num, res)
            if pos >= len(res):
                res.append(num)
            else:
                res[pos] = num
    
        return len(res)
    
    

    def binarySearch(self, target, nums):
        """
        return type: int (ceiling of the insert position)
        """
        if not nums:
            return 0
    
        l = len(nums)
        start = 0
        end = l - 1
    
        while start <= end:
            half = start + (end - start) // 2
            if nums[half] == target:
                return half
            elif nums[half] < target:
                start = half + 1
            else:
                end = half - 1
        
        return start


if __name__ == '__main__':
    envelopes = [[5,4], [6,4], [6,7], [2,3]]
    case = Solution()
    print case.maxEnvelopes(envelopes)
