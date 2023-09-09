class AllOne:
    def __init__(self):
        self.a={}
        self.min=100000
        self.max=0
        self.minstack=[]
        self.maxstack=[]

    def inc(self,k):
        if k in self.a:
            self.a[k]+=1
        else:
            self.a[k]=1
        self.maxstack=[]
        self.minstack=[]

    def dec(self,k):
        self.a[k]-=1
        if self.a[k]<=0:
            del self.a[k]
        self.maxstack=[]
        self.minstack=[]

    def getMaxKey(self):
        if self.maxstack:
            return self.maxstack[-1]
        m=v=0
        for i in self.a:
            if self.a[i]>m:
                m=self.a[i]
                v=i
        if v and m>=self.max:
            self.max=m
            self.maxstack.append(v)
        return v or ''

    def getMinKey(self):
        if self.minstack:
            return self.minstack[-1]
        m=float('inf')
        v=0
        for i in self.a:
            if self.a[i]<m:
                m=self.a[i]
                v=i
        if v and m<=self.min:
            self.min=m
            self.minstack.append(v)
        return v or ''

a=AllOne()

print(a.inc('hello'))
print(a.inc('hello'))

print(a.getMaxKey())
print(a.getMinKey())

print(a.inc('leet'))

print(a.getMaxKey())
print(a.getMinKey())

print(a.a)