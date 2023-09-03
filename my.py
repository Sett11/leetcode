class Solution:
    def summaryRanges(self,a):
        r=[]
        while a:
            t=[a.pop(0)]
            while a:
                if a[0]-t[-1]==1:
                    t.append(a.pop(0))
                else:
                    break
            r.append(f'{t[0]}->{t[-1]}'if len(t)>1 else str(t[0]))
        return r
    
s=Solution()

print(s.summaryRanges([0,2,3,4,6,8,9]))