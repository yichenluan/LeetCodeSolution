class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        temp_res = self.myPow(x, n / 2)
        if n % 2:
            return  temp_res * temp_res * x
        return temp_res * temp_res
