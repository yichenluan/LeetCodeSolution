class Solution(object):
    def deserialize(self, s):
        def nestedInteget(x):
            if isinstance(x, int):
                return NestedInteger(x)
            lst = NestedInteger()
            for y in x:
                lst.add(nestedInteget(y))
            return lst
        return nestedInteget(eval(s))
