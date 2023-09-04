class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self,v):
        self.stack.append(v)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)
    
m=MinStack()

m.push(-2)
m.push(0)
m.push(-3)

print(m.getMin())

m.pop()

print(m.top())