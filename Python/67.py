class Solution(object):
    def addBinary(self, a, b):
        pa = len(a) - 1
        pb = len(b) - 1
        c = 0
        res = ''
        while pa >= 0 or pb >= 0 or c > 0:
            c += 1 if pa >= 0 and a[pa] == '1' else 0
            c += 1 if pb >= 0 and b[pb] == '1' else 0
            res = str(c % 2) + res
            pa, pb, c = pa -1, pb - 1, c / 2
        return res
