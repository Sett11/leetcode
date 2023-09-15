class MyCircularDeque:
    def __init__(self, k):
        self.max_size = k
        self.deck = []

    def insertFront(self, v):
        if len(self.deck) < self.max_size:
            return not bool(self.deck.insert(0, v))
        return False

    def insertLast(self, v):
        if len(self.deck) < self.max_size:
            return not bool(self.deck.append(v))
        return False

    def deleteFront(self):
        if self.deck:
            return bool(str(self.deck.pop(0)))
        return False

    def deleteLast(self):
        if self.deck:
            return bool(str(self.deck.pop()))
        return False

    def getFront(self):
        try:
            return self.deck[0]
        except:
            return -1

    def getRear(self):
        try:
            return self.deck[-1]
        except:
            return -1

    def isEmpty(self):
        return not bool(self.deck)

    def isFull(self):
        return self.max_size == len(self.deck)


m = MyCircularDeque(5)

print(m.insertFront(9))
print(m.insertLast(11))
print(m.deck)
print(m.isEmpty())