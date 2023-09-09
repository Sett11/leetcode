class Solution:
    def countSymmetricIntegers(self,l,r):
        c=0
        i=l
        while i<=r:
            if i==101:
                i=1001
            j=str(i)
            l=len(j)//2
            if sum([int(k) for k in j[l:]])==sum([int(k) for k in j[:l]]):
                c+=1
            i+=1
        return c
    
s=Solution()

print(s.countSymmetricIntegers(1,100))