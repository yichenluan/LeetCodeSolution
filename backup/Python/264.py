class Solution(object):
    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        nums = [1]
        two_point = 0
        three_point = 0
        five_point = 0
        index = 1
        while True:
            two_next = 2 * nums[two_point]
            three_next = 3 * nums[three_point]
            five_next = 5 * nums[five_point]
            min_next = min(two_next, three_next, five_next)
            if two_next == min_next:
                two_point += 1
            if three_next == min_next:
                three_point += 1
            if five_next == min_next:
                five_point += 1
            nums.append(min_next)
            index += 1
            if index == n:
                return min_next


if __name__ == '__main__':
    n = 10
    case = Solution()
    print case.nthUglyNumber(n)
