class CustomStack:
    def __init__(self,m):
        self.max_size=m
        self.stack=[]

    def push(self,x):
        if len(self.stack)<self.max_size:
            self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self,k,v):
        self.stack=[i+v for i in self.stack[:k]]+self.stack[k:]

c=CustomStack(3)

print(c.push(1))
print(c.push(2))
print(c.pop())
print(c.push(2))
print(c.push(3))
print(c.push(4))
print(c.stack)
print(c.increment(5,100))
print(c.stack)
print(c.increment(2,100))
print(c.stack)
print(c.pop())
print(c.pop())
print(c.pop())
print(c.pop())