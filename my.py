def summaryRanges(l):
        r=[]
        a=sorted(set(l))
        while a:
            t=[a.pop(0)]
            while a:
                if a[0]-t[-1]==1:
                    t.append(a.pop(0))
                else:
                    break
            r.append([t[0],t[-1]])
        return r

class SummaryRanges:
    def __init__(self):
        self.a=[]

    def addNum(self,v):
        self.a.append(v)

    def getIntervals(self):
        return summaryRanges(self.a)

s=SummaryRanges()

s.addNum(1)
print(s.getIntervals())
s.addNum(3)
print(s.getIntervals())
s.addNum(7)
print(s.getIntervals())
s.addNum(2)
print(s.getIntervals())
s.addNum(6)
s.addNum(6)
s.addNum(6)
print(s.getIntervals())