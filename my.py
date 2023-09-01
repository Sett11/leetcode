class MyStack:

    def __init__(self):
        self.a=[]

    def push(self,x):
        self.a.append(x)

    def pop(self):
        return self.a.pop()

    def top(self):
        return self.a[-1]

    def empty(self):
        return not self.a