class Solution(object):
    def guessNumber(self, n):
        l = 1
        r = n
        while l <= r:
            mid = (l + r) / 2
            guess_res = guess(mid)
            if guess_res == 0:
                return mid
            if guess_res == 1:
                l = mid + 1
            else:
                r = mid - 1
        return l
