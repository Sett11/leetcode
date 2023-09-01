class MyQueue:

    def __init__(self):
        self.a=[]

    def push(self,x):
        self.a.append(x)

    def pop(self):
        return self.a.pop(0)

    def peek(self):
        return self.a[0]

    def empty(self):
        return not self.a