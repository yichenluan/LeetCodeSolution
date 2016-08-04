class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        res = [1]
        len_p = len(primes)
        index = [0 for i in range(len_p)]
        next_ans = [num for num in primes]
        test = 1
        count = 1
        while True:
            for i in range(len_p):
                while next_ans[i] == min(next_ans):
                    if next_ans[i] != res[-1]:
                        if count == n:
                            return res[-1]
                        res.append(next_ans[i])
                        count += 1
                    index[i] += 1
                    next_ans[i] = primes[i] * res[index[i]]

if __name__ == '__main__':
    n = 12
    primes = [2, 7, 13, 19]
    case = Solution()
    print case.nthSuperUglyNumber(n, primes)
