class Solution:
    def decrypt(self,a,k):
        if not k:
            return [0]*len(a)
        b=a+a+a
        l=len(a)
        r=[]
        for i in range(l,l+l):
            if k>0:
                r.append(sum(b[i:i+k]))
            else:
                r.append(sum(b[i+k:i]))
        if k>0:
            r.append(r.pop(0))
        return r
    
s=Solution()

print(s.decrypt([5,7,1,4],3))
print(s.decrypt([2,4,9,3],-2))