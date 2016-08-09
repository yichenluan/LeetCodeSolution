class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.colletion = list()
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.colletion:
            res = False
        else:
            res = True
        self.colletion.append(val)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.colletion:
            return False
        self.colletion.remove(val)
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        n = len(self.colletion)
        return self.colletion[random.randint(0, n - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
