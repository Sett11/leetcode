class Solution:
    def maximumTripletValue(self,a):
        l=len(a)
        m=0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    m=max(m,(a[i]-a[j])*a[k])
        return m
    
s=Solution()

print(s.maximumTripletValue([12,6,1,2,7]))