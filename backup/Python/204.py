class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [0, 0] + [1] * (n - 2)
        
        for i in xrange(2, int(n ** 0.5) + 1):
            if is_prime[i] == 1:
                is_prime[i**2::i] = [0] * len(is_prime[i**2::i])

        return sum(is_prime)
