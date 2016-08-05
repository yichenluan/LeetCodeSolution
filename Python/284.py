class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.hasPeeked = False
        self.peekedElement = None

    def next(self):
        if not self.hasPeeked:
            return self.iterator.next()
        result = self.peekedElement
        self.hasPeeked = False
        self.peekedElement = None
        return result

    def peek(self):
        if not self.hasPeeked:
            self.peekedElement = self.iterator.next()
            self.hasPeeked = True
        return self.peekedElement

    def hasNext(self):
        return self.hasPeeked or self.iterator.hasNext()
