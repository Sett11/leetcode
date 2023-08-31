class Solution:
    def intersect(self,a,b):
        s=set(a+b)
        r=[]
        for i in s:
            if all([i in a, i in b]):
                r.extend([i]*min(a.count(i),b.count(i)))
        return r
    
s=Solution()

print(s.intersect([1,2,2,1],[2,2]))