class Solution:
    def mostFrequent(self,a,n):
        b=[a[i+1] for i,j in enumerate(a) if j==n and i!=len(a)-1]
        s,o,m=set(b),{},0
        for i in s:
            t=b.count(i)
            o[t],m=i,max(t,m)
        return o[m]
    
s=Solution()

print(s.mostFrequent([1,100,200,1,100],1))
print(s.mostFrequent([2,2,2,2,3],2))