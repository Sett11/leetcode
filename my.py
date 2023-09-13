class Solution:
    def minimumAbsDifference(self,a):
        a.sort()
        m=int(1e9)
        o={}
        for i in range(0,len(a)-1,1):
            q=[a[i],a[i+1]]
            s=abs(a[i]-a[i+1])
            m=min(s,m)
            if s in o:
                o[s].append(q)
            else:
                o[s]=[q]
        return o[m]

s=Solution()

print(s.minimumAbsDifference([4,2,1,3]))
print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
print(s.minimumAbsDifference([1,3,6,10,15]))