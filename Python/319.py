'''Bulb Switcher

找规律很好找，关键在于思维够不够深入，很容易满足于找到的表象，
然后忽略了深层次的理解，只有那些平分数才有奇数个分解因子，而这些数，
只需要开根号就得到了数目。
'''
class Solution(object):
    def bulbSwitch(self, n):
        return int(n ** 0.5)
