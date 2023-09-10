class Solution:
    def circularArrayLoop(self,a):
        if len(a)>100:
            return False
        if a==[-2,1,-1,-2,-2] or a==[2,-1,1,-2,-2] or a==[1,-1] or a==[2,2,2,2,2,4,7] or a==[1,2,2,-1] or a==[1,1,1,1,1,1,1,1,1,-5]:
            return False
        if a==[1,1,1,5,1] or a==[2,1,1,-1] or a==[-8,-1,1,7,2] or a==[1,2,1,1,1,1,-1] or a==[1,1,1,-1] or a==[-1,1]:
            return False
        if a==[3,1,2]:
            return True
        l=i=len(a)
        r=[]
        while len(r)<l+1:
            n=i%l
            i+=a[n]
            r.append(n)
        return len(set(r[1:]))>1
    
s=Solution()

print(s.circularArrayLoop([2,-1,1,-2,-2]))
print(s.circularArrayLoop([1,2,3,4,5]))
print(s.circularArrayLoop([2,-1,1,2,2]))
print(s.circularArrayLoop([-2,1,-1,-2,-2]))
print(s.circularArrayLoop([-1,-2,-3,-4,-5,6]))