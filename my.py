class Solution:
    def findTheArrayConcVal(self,a):
        l=len(a)//2
        b,c=a[:l],a[l:][::-1]
        if len(b)<len(c):
            b+=[0]
        if len(c)<len(b):
            c+=[0]
        return sum([int(str(b[i])+str(c[i])) for i in range(len(b))])
    
s=Solution()

print(s.findTheArrayConcVal([7,52,2,4]))
print(s.findTheArrayConcVal([5,14,13,8,12]))