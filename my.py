class Solution:
    def prefixesDivBy5(self,a):
        c=''
        for i in range(len(a)):
            c+=str(a[i])
            a[i]=int(c,2)%5==0
        return a
            
    
s=Solution()

print(s.prefixesDivBy5([0,1,1]))