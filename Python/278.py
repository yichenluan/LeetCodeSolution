class Solution(object):
    def firstBadVersion(self, n):
        start, end = 1, n+1
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
