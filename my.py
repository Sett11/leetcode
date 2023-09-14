class Solution:
    def longestMountain(self,a):
        a.append(a[-1]+1)
        l=len(a)
        m=0
        for i in range(l-1):
            v=False
            k=-1
            if a[i]<a[i+1]:
                for j in range(i+1,l):
                    if j==l-1:
                        if a[j]<=a[j-1]:
                            m=max(len(a[i:j]),m)
                        break
                    if v and a[j]<=a[j+1]:
                        t=a[i:j+1]
                        if t.count(a[k])==1:
                            m=max(m,len(t))
                        i=j
                        break
                    if not v and a[j]>=a[j+1]:
                        v=True
                        k=j
        return m
    
s=Solution()

print(s.longestMountain([2,1,4,7,3,2,5]))
print(s.longestMountain([2,3]))
print(s.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))
print(s.longestMountain([0,2,0,2,1,2,3,4,4,1]))
print(s.longestMountain([0,2,0,0,2,0,2,1,1,0,2,1,0,0,1,0,2,1,2,0,1,1,0,2,2,1,2,2,0,0,0,1,0,2,0,0,1,2,0,1,0,2,0,2,0,0,0,0,2,1,0,0,0,0,1,0,2,1,2,2,1,0,0,1,0,2,0,0,0,2,1,0,1,2,1,0,1,0,2,1,0,2,0,2,1,1,2,0,1,0,1,1,1,1,2,1,2,2,2,0]))