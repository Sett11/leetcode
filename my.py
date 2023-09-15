class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, v):
        self.queue.insert(0, v)

    def pushMiddle(self, v):
        l = len(self.queue)//2
        self.queue = self.queue[0:l]+[v]+self.queue[l:]
        return self.queue

    def pushBack(self, v):
        self.queue.append(v)

    def popFront(self):
        try:
            return self.queue.pop(0)
        except:
            return -1

    def popMiddle(self):
        l = len(self.queue)//2
        try:
            return self.queue.pop(l if len(self.queue)&1 else l-1)
        except:
            return -1

    def popBack(self):
        try:
            return self.queue.pop()
        except:
            return -1


f = FrontMiddleBackQueue()

f.pushMiddle(3)
f.pushFront(6)
f.pushMiddle(6)
f.pushMiddle(3)
print(f.queue)
print(f.popMiddle())
print(f.popMiddle())
# print(f.queue)
# print(f.popMiddle())
# print(f.popMiddle())