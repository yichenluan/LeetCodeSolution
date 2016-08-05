class Queue(object):
    def __init__(self):
        self.queue = list()

    def push(self, x):
        self.queue.insert(0, x)

    def pop(self):
        self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def empty(self):
        if not self.queue:
            return True
        return False
