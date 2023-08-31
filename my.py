class Solution:
    def merge(self,a):
        a=sorted(a,key=lambda e:(e[0],e[1]))
        i=0
        while i<len(a)-1:
            if a[i][0]<=a[i+1][0] and a[i][1]<=a[i+1][1] and a[i][1]>=a[i+1][0]:
                a[i][1]=a[i+1][1]
                a.pop(i+1)
                i-=1
            if len(a)==1:
                break
            if a[i][0]<=a[i+1][0] and a[i][1]>=a[i+1][1]:
                a.pop(i+1)
                i-=1
            i+=1
        return a
    
s=Solution()

print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[2,3]]))
print(s.merge([[1,4],[1,5]]))