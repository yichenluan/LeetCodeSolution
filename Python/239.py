class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # maitain a max heap
        heap, result = [], []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (-n, i))
            if i >= k - 1:
                # remove all out of range max values
                while heap[0][1] + k <= i:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result
