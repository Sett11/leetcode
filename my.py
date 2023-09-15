class MyCircularQueue:
    def __init__(self,k):
        self.max_size=k
        self.queue=[]

    def enQueue(self,v):
        if len(self.queue)<self.max_size:
            return not bool(self.queue.append(v))
        return False

    def deQueue(self):
        try:
            return bool(str(self.queue.pop(0)))
        except:
            return False

    def Front(self):
        try:
            return self.queue[0]
        except:
            return -1

    def Rear(self):
        try:
            return self.queue[-1]
        except:
            return -1

    def isEmpty(self):
        return not bool(self.queue)

    def isFull(self):
        return len(self.queue)>=self.max_size
    
m=MyCircularQueue(3)

print(m.enQueue(1))
print(m.enQueue(2))
print(m.enQueue(3))

print(m.queue)