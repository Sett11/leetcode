class Solution:
    def hIndex(self,a):
        m=max(a)
        while m:
            t=[i for i in a if i>=m]
            if len(t)>=m:
                return m
            m-=1
        return m 
    
s=Solution()

print(s.hIndex([3,0,6,1,5]))