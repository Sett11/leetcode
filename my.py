class Solution:
    def equalFrequency(self,s):
        if len(set(s))==1:
            return True
        a=sorted([s.count(i) for i in set(s)])
        return (len(set(a[:-1]))==1 and a[-1]-a[0]==1) or (len(set(a))==1 and a[0]==1) or ((1 in a and a.count(1)==1) and len(set([i for i in a if i!=1]))==1)

s=Solution()

print(s.equalFrequency('zz'))