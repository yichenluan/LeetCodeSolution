class Solution(object):
    def merge(self, intervals):
        def helper(interval1, interval2):
            if interval1.start > interval2.start:
                return 1
            elif interval1.start == interval2.start and interval1.end > interval2.end:
                return 1
            else:
                return -1
        intervals = sorted(intervals, helper)
        n = len(intervals)
        if n <= 1:
            return intervals
        i = 1
        while i < n:
            if intervals[i].start <= intervals[i-1].end:
                intervals[i-1].end = max(intervals[i].end, intervals[i-1].end)
                del(intervals[i])
                n -= 1
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    intervals = [[2,6], [1,3], [8,10], [15,18]]
    case = Solution()
    print case.merge(intervals)
