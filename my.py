class Solution:
    def singleNumber(self,a):
        s=set(a)
        r=[]
        for i in s:
            if len(r)==2:
                return r
            if a.count(i)==1:
                r.append(i)
        return r
    
s=Solution()

print(s.singleNumber([1,2,1,3,2,5]))